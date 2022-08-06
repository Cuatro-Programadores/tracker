from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from http import server
import smtplib
import requests
import json
import dotenv
import os
import ssl
from twilio.rest import Client


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

    # def send_notification(self, phone_number, cell_carrier, message, original_url):
    #     short_url = self.shorten_link(original_url)
    #     full_message = message + short_url
    #     phone_number_str = str(phone_number)
    #     sms_gate = self.carrier_dict[f"{cell_carrier}"]
    #     password = os.environ.get("EMAIL_PASSWORD")
    #     smtp_server = "smtp.gmail.com"
    #     sender_email = os.environ.get("SENDER_EMAIL")
    #     receiver_email = phone_number_str + sms_gate

    #     msg = MIMEMultipart('alternative')
    #     msg['From'] = sender_email
    #     msg['To'] = receiver_email

    #     part1 = MIMEText(full_message, 'plain')

    #     msg.attach(part1)
    #     context = ssl.create_default_context()
    #     with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
    #         server.login(sender_email, password)
    #         server.sendmail(sender_email, receiver_email, msg.as_string())

        # mail.ehlo()

        # mail.starttls()

        # mail.login(sender_email, password)
        # mail.sendmail(sender_email, receiver_email, msg.as_string())
        # mail.quit()


if __name__ == "__main__":
    pass
