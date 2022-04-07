import os
import requests
from bs4 import BeautifulSoup
import smtplib
from export_credentials import ExportCredentials

export_cred = ExportCredentials().setup_environment()

CHAIR_URL = "https://www.amazon.com/BZLSFHZ-Ergonomic-Adjustable-Headrest-Breathable/dp/B09MB1QT4G/ref=sr_1_206?crid" \
            "=1BTMETGBD2VVO&keywords=chairs+for+desk&qid=1649319961&sprefix=chairs%2Caps%2C394&sr=8-206 "
BAND_URL = "https://www.amazon.com/TalkWorks-Compatible-Stainless-Adjustable-Magnetic/dp/B0866BKBK8/ref" \
           "=pd_pb_ss_no_hpb_sccl_1/140-0619034-7057416?pd_rd_w=ZzDY0&pf_rd_p=45f92aae-3fbe-4e26-9929-951264041217" \
           "&pf_rd_r=N89FZ7Q4EV7PS7N6RMK5&pd_rd_r=9a635269-9908-4b39-996f-7d789898eb18&pd_rd_wg=vE6AZ&pd_rd_i" \
           "=B0866BKBK8&psc=1 "

CHAIR_PRICE_TARGET = 4000.00
BAND_PRICE_TARGET = 18

MAIL_SERVER = os.environ.get('MAIL_SERVER')
MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')

def get_item_details_for(item_url):
    # Returns title, price as float, and url for item
    headers = {
        'Accept-Language': 'en-GB,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0',
    }

    response = requests.get(item_url, headers=headers)

    soup = BeautifulSoup(response.content, "lxml")
    item_price_no_currency = soup.find("span", "a-offscreen").getText().split("$")[1]
    item_price_no_commas = item_price_no_currency.replace(",", "")
    item_price = float(item_price_no_commas)

    # Remove white-space from item_title string with strip() method
    item_title = soup.find("div", id="titleSection").span.getText().strip()
    # print(f"title is: {item_title}")
    return item_title, item_price, item_url


def send_email(msg, to_address):
    with smtplib.SMTP(MAIL_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=to_address,
                            msg=msg
                            )


def create_msg(title, price, link):
    # Returns formatted email message ready to send
    msg = f"Subject: Price Alert!\n\n{title}\nis now selling for ${price}.\n" \
          f"Click the following link to purchase.\n{link} "
    return msg


item_details = get_item_details_for(CHAIR_URL)

if item_details[1] < CHAIR_PRICE_TARGET:
    # send an email to self with the title of the product,
    #   the current price,
    #   and a link to buy.
    print("Preparing message...")
    message = create_msg(title=item_details[0], price=item_details[1], link=item_details[2])
    print("Sending message...")
    send_email(msg=message, to_address=MY_EMAIL)
else:
    print(f"The price of {item_details[1]} is not less than target {CHAIR_PRICE_TARGET}" )
    print("No price drops to report.")
