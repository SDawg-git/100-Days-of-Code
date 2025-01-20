import bs4
import requests
from bs4 import BeautifulSoup
import smtplib

practice_URL = "https://appbrewery.github.io/instant_pot/"
live_URL = "https://amzn.eu/d/1sx445c"

SMTP_PASSWORD = os.environ.get["SMTP_PASS"]               #for gmail
MY_EMAIL = os.environ.get["EMAIL"]

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0"
}

response = requests.get(url=practice_URL, headers=headers)
response.raise_for_status()
website = response.text

#print(website)

soup = BeautifulSoup(website, "html.parser")

main_price = soup.find(class_="a-price-whole").text
second_price = soup.find(class_="a-price-fraction").text

current_item_price = round(float(main_price+second_price))
lowest_item_price = 120

#print(f"The price is £{current_item_price}")

if current_item_price < lowest_item_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=SMTP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=os.environ.get["RECEIPIENT"],  #t3st_python@yahoo.com
                            msg=f"Subject: Price Drop!\n\n The price has dropped by £{lowest_item_price-current_item_price} to £{current_item_price}")
