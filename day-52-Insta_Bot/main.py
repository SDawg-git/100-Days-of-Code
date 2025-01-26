import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

INSTA_NAME = os.environ.get["INSTA_NAME"]
INSTA_PASS = os.environ.get["INSTA_PASS"]
INSTA_EMAIL = os.environ.get["INSTA_EMAIL"]
SIMILAR_ACC = os.environ.get["TARGET_ACC"]
SALADS_LINK = os.environ.get["TARGET_LINK"]



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-extensions")



class InstaFollower:
    def __init__(self):

        self.driver = webdriver.Chrome(options=chrome_options)


    def login(self):

        self.driver.get(url="https://www.instagram.com/accounts/login/")
        time.sleep(2)
        decline_cookies = self.driver.find_element(By.CSS_SELECTOR, "button._a9--._ap36._a9_1")
        decline_cookies.click()

        time.sleep(1)

        # login_button = self.driver.find_element(By.LINK_TEXT, "Log in")
        # login_button.click()


        email_input = self.driver.find_element(By.NAME, "username")
        email_input.send_keys(INSTA_EMAIL)

        pass_input = self.driver.find_element(By.NAME, "password")
        pass_input.send_keys(INSTA_PASS)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-._ap30')
        submit_button.click()

        time.sleep(5)

    def find_followers(self):

        # not_now = self.driver.find_element(By.XPATH, "//div[text()='Not now']")
        # not_now.click()

        self.driver.get("https://www.instagram.com/saladtff/following/")

        time.sleep(1)

        followers_link = self.driver.find_element(By.CSS_SELECTOR, "section ul li:nth-child(3) a")
        followers_link.click()

        time.sleep(2)

        # all_followers = self.driver.find_elements(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div')
        # for follower in all_followers:
        #     print(follower.text)

        iframe = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]')
        scroll_origin = ScrollOrigin.from_element(iframe)
        for i in range(2):                                          #change to however many scrolls you want
            ActionChains(self.driver) \
                .scroll_from_origin(scroll_origin, 0, 5000) \
                .perform()
            time.sleep(2)

        # all_followers = self.driver.find_elements(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div')
        # for follower in all_followers:
        #     print(follower.text)

    def follow(self):


        while True:                                                     #follows everyone, then unfollows constantly

            follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            for button in follow_buttons:
                if button.text == "Follow":
                    button.click()

            unfollow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            for button in unfollow_buttons:
                if button.text == "Following" or button.text == "Requested":
                    button.click()



bot = InstaFollower()

bot.login()
bot.find_followers()
#bot.follow()                       #turned it off for now to not embarass salad anymore

