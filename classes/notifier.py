import requests
import json
import dotenv
import os
from twilio.rest import Client


dotenv.load_dotenv(dotenv.find_dotenv())


class Notifier():

    def shorten_link(self, link):
        api_key = os.environ.get("API_KEY")
        linkRequest = {
            "destination": f"{link}",
            "domain": {"fullName": "rebrand.ly"}

        }

        requestHeaders = {
            "Content-type": "application/json",
            "apikey": f"{api_key}",

        }

        r = requests.post("https://api.rebrandly.com/v1/links",
                          data=json.dumps(linkRequest),
                          headers=requestHeaders)

        if (r.status_code == requests.codes.ok):
            link = r.json()
            return link["shortUrl"]
        else:
            return "error"

    def send_notification(self, phone_number, message, original_url):

        sender_number = os.environ['SENDER_PHONE_NUMBER']
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        short_url = self.shorten_link(original_url)
        full_message = message + short_url

        message = client.messages \
            .create(
                body=f"{full_message}",
                from_=f'{sender_number}',
                to=f'{phone_number}'
            )
