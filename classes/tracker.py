import schedule
import time
import dotenv
import os
from pymongo import MongoClient
from bson.json_util import dumps, loads
from scraper import Scraper
from notificator import Notificator

dotenv.load_dotenv(dotenv.find_dotenv())


password = os.environ.get("MONGO_PASSWORD")


class Tracker():
    def __init__(self):
        self.connection = MongoClient(
            f"mongodb+srv://mypricescout:{password}@my-price-scout-users.yugh3.mongodb.net/?retryWrites=true&w=majority")
        self.scraper = Scraper()
        self.notificator = Notificator()

    def get_all_users(self):

        retrieved_users_cursor = self.connection.user_data.user_data.find({})
        user_list_cursor = list(retrieved_users_cursor)
        json_user_list = dumps(user_list_cursor)
        user_list = loads(json_user_list)

        return user_list

    def update_all_users(self):
        user_list = self.get_all_users()

        for user in user_list:
            for product in user["watchlist"]:
                target_price = float(product["target_price"])
                product_name = product["name"]
                for specific_product in product["specific_product_list"]:

                    # specific_product_website = specific_product["website"]
                    specific_product_url = specific_product["url"]
                    specific_product_price = float(specific_product["price"])
                    notification_message = f"Desired price of ${target_price} found for your item '{product_name}' at:\n"

                    if specific_product_price <= target_price:
                        if product["is_product_being_tracked"] == True:
                            self.notificator.send_notification(
                                user["phone_number"], user["cell_carrier"], notification_message, specific_product_url)
                            product["is_product_being_tracked"] = False
                    if specific_product["website"] == "Amazon":
                        scrape_attempt = self.scraper.scrape_amazon(
                            specific_product["url"])
                        if scrape_attempt != 999999:
                            specific_product["price"] = scrape_attempt
                        else:
                            continue

                    if specific_product["website"] == "Target":
                        specific_product["price"] = self.scraper.scrape_target(
                            specific_product["url"])

        return user_list

    def update_and_save_users_to_db(self):

        updated_user_list = self.update_all_users()
        if updated_user_list:
            self.connection.user_data.user_data.delete_many({})
            self.connection.user_data.user_data.insert_many(updated_user_list)


if __name__ == "__main__":

    tracker = Tracker()
    track = tracker.update_and_save_users_to_db
    schedule.every(5).seconds.do(track)

    while True:
        schedule.run_pending()
        time.sleep(1)
