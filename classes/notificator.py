from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
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

    def send_notification(self, phone_number, cell_carrier, message):

        phone_number_str = str(phone_number)
        sms_gate = self.carrier_dict[f"{cell_carrier}"]
        port = 465  # For SSL
        password = os.environ.get("EMAIL_PASSWORD")
        smtp_server = "smtp.gmail.com"
        sender_email = os.environ.get("SENDER_EMAIL")
        receiver_email = phone_number_str + sms_gate

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)


if __name__ == "__main__":
    notificator = Notificator()
    msg = "hello"
    notificator.send_notification(
        9079572741, "ATT", msg)
