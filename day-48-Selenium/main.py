import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://orteil.dashnet.org/cookieclicker/"

driver = webdriver.Chrome(options=chrome_options)

driver.get(url=URL)




consent = driver.find_element(By.CLASS_NAME, value="fc-button")
consent.click()

time.sleep(1)

language_select = driver.find_element(By.ID, value="langSelect-EN")
language_select.click()

time.sleep(3)


cookie = driver.find_element(By.ID, value="bigCookie")




timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        cursor = driver.find_element(By.ID, value="product0")
        if driver.find_element(By.ID, value="cookies").text > driver.find_element(By.ID, value="productPrice0").text:
            cursor.click()
