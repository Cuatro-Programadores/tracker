# carrier_dict = {
#             "ATT": "@txt.att.net",
#             "BOOST": "@sms.myboostmobile.com",
#             "CRICKET": "@sms.cricketwireless.net",
#             "GOOGLEFI": "@msg.fi.google.com",
#             "METROPCS": "@mymetropcs.com",
#             "MINT": "@mailmymobile.net",
#             "SIMPLEMOBILE": "@smtext.com",
#             "SPRINT": "@messaging.sprintpcs.com",
#             "TMOBILE": "@tmomail.net",
#             "VERIZON": "@vtext.com",
#             "VIRGIN": "@vmobl.com",
#             "XFINITY": "@vtext.com"
#         }


# WORK IN PROGRESS

# def scrape_walmart(self, url):

#     URL = url

#     # options = webdriver.ChromeOptions()
#     # # options.add_argument("start-maximized")
#     # options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
#     # chrome_driver_binary = "\home\s14mx\bin\chromedriver"

#     # driver = webdriver.Chrome(
#     #     executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe")
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.binary_location = '/usr/bin/chromedriver'
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument('--no-sandbox')
#     driver = webdriver.Chrome(
#         executable_path='/usr/bin/chromedriver',
#         chrome_options=chrome_options)
#     # driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get(URL)
#     page = driver.page_source
#     driver.close()

#     finds = re.findall(
#         r'submapType\"\:null},\"currentPrice\"\:{\"price\"\:\d+(?:\.\d+)?', page)

#     item_found = []

#     for find in finds:
#         item_found.append(find)

#     if item_found is None:
#         actual_price = "Price not available"
#         return actual_price
#     else:
#         actual_price = re.findall(r'\d+(?:\.\d+)?', item_found[0])
#         print(float(actual_price[0]))
#         return (float(actual_price[0]))

# SMTP FREE EMAIL/TEXT MESSAGE

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
