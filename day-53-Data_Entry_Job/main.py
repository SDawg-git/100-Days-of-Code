import time

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import bs4
from selenium.webdriver.common.by import By

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfyczn0NWzo2DKXQnFQ0-YmhWqgN-wSsViQRWm9s_d2_QgUkQ/viewform?usp=dialog"
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"



r = requests.get(ZILLOW_LINK)
content = r.content
soup = BeautifulSoup(content, features="html.parser")
#print(soup.prettify())


addresses = []
links = []
prices = []


all_addresses = soup.find_all("address")

for address in all_addresses:
    #print(address.text)
    #current_address = address.text.replace("\n", "")
    addresses.append(address.text.strip())

#print(addresses)



all_links = soup.find_all(class_="property-card-link")

for link in all_links:
    #print(link["href"])
    links.append(link["href"])



all_prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")

for price in all_prices:
    current_price = price.text
    current_price = current_price.removeprefix("$")
    current_price = current_price[:5]
    clean_price = current_price.replace(",", "")        #might also have to replace "+" with " "
    prices.append(f"£{clean_price}")

print(addresses)
print(links)
print(prices)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url=FORM_LINK)

time.sleep(1)



for position in range(len(addresses)):
    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    inputs[0].send_keys(addresses[position])
    inputs[1].send_keys(prices[position])
    inputs[2].send_keys(links[position])
    button = driver.find_element(By.XPATH, "//div[@role='button' and .//span[text()='Submit']]")
    button.click()
    time.sleep(1)
    next_form = driver.find_element(By.XPATH, "//a[text()='Submit another response']")
    next_form.click()
    time.sleep(1)

driver.quit()



