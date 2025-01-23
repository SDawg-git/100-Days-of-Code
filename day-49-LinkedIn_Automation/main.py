from selenium import webdriver
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
import time
from selenium_stealth import stealth

LINKEDIN_LINK = "https://www.linkedin.com/jobs/search/?currentJobId=4083021297&f_AL=true&geoId=90009496&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
#LINKEDIN_LINK = "https://www.linkedin.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])   #stealth test
chrome_options.add_experimental_option('useAutomationExtension', False)             #stealth test


driver = webdriver.Chrome(chrome_options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

#driver.get(url=LINKEDIN_LINK)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

#nsm7Bb-HzV7m-LgbsSe-bN97Pc-sM5MNb oXtfBe-l4eHX
#nsm7Bb-HzV7m-LgbsSe-BPrWId
#authwall-join-form__form-toggle--bottom form-toggle

#sign_in = driver.find_element(By.CLASS_NAME, value="authwall-join-form__form-toggle--bottom")
#sign_in = driver.find_element(By.CSS_SELECTOR, "div form p button")

#sign_in = driver.find_element(By.XPATH, "//*[@id='main-content']/div[1]/form/p/button")
time.sleep(4)
#sign_in_google = driver.find_element(By.XPATH, "//*[@id='container']/div/div[1]")
#sign_in_google = driver.find_element(By.ID, "button-label")
sign_in = driver.find_element(By.XPATH, value="//*[@id='base-contextual-sign-in-modal']/div/section/div/div/div/div[2]/button")

sign_in.click()
