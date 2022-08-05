from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.text import MIMEText
import smtplib
import requests
import json
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())


class Notificator():
    def __init__(self):
        self.carrier_dict = {
            "ATT": "@txt.att.net",
            "BOOST": "@sms.myboostmobile.com",
            "CRICKET": "@sms.cricketwireless.net",
            "GOOGLEFI": "@msg.fi.google.com",
            "METROPCS": "@mymetropcs.com",
            "MINT": "@mailmymobile.net",
            "SIMPLEMOBILE": "@smtext.com",
            "SPRINT": "@messaging.sprintpcs.com",
            "TMOBILE": "@tmomail.net",
            "VERIZON": "@vtext.com",
            "VIRGIN": "@vmobl.com",
            "XFINITY": "@vtext.com"
        }

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

    def send_notification(self, phone_number, cell_carrier, message, original_url):
        short_url = self.shorten_link(original_url)
        full_message = message + short_url
        phone_number_str = str(phone_number)
        sms_gate = self.carrier_dict[f"{cell_carrier}"]
        password = os.environ.get("EMAIL_PASSWORD")
        smtp_server = "smtp.gmail.com"
        sender_email = os.environ.get("SENDER_EMAIL")
        receiver_email = phone_number_str + sms_gate

        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = receiver_email

        part1 = MIMEText(full_message, 'plain')

        msg.attach(part1)

        mail = smtplib.SMTP(smtp_server, 587)

        mail.ehlo()

        mail.starttls()

        mail.login(sender_email, password)
        mail.sendmail(sender_email, receiver_email, msg.as_string())
        mail.quit()


if __name__ == "__main__":
    notificator = Notificator()
    # # msg = "hello"
    notificator.send_notification(
        9079572741, "ATT", "Desired price of $300 found for your item 'TV' at:\n https://www.target.com/", "")

    # print(notificator.shorten_link(
    #     "https://www.amazon.com/APC-Battery-Protector-BackUPS-BX1500M/dp/B06VY6FXMM?ref_=Oct_DLandingS_D_d1d1e0d6_60&smid=ATVPDKIKX0DER&th=1"))
    pass
