from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#195180f46763dbc73.3657482405

PROMISED_DOWN = 230
PROMISED_UP = 10
TWITTER_EMAIL = os.environ.get["EMAIL"]
TWITTER_PASSWORD = os.environ.get["PASS"]
TWITTER_URL = "https://x.com/SDawgPy"
TWITTER_USERNAME = "SDawgPy"
SPEED_TEST_URL = "https://www.speedtest.net"



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = ""
        self.up = ""



    def get_internet_speed(self):
        self.driver.get(url=SPEED_TEST_URL)
        time.sleep(1)
        reject_all = self.driver.find_element(By.ID, 'onetrust-reject-all-handler')
        reject_all.click()
        #go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a') #XPATH is bad practice, need to use CSS selectors more
        go_button = self.driver.find_element(By.CSS_SELECTOR, '.start-button a')
        go_button.click()
        time.sleep(40)
        self.down = self.driver.find_element(By.CSS_SELECTOR, '.result-data-large.number.result-data-value.download-speed').text
        self.up = self.driver.find_element(By.CSS_SELECTOR, '.result-data-large.number.result-data-value.upload-speed').text
        print(self.down)
        print(self.up)


    def tweet_at_provider(self):
        self.driver.get(url=TWITTER_URL)
        time.sleep(3)
        email_input = self.driver.find_element(By.CSS_SELECTOR, 'input')
        email_input.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()
        time.sleep(2)

        ### NEED TRY AND CATCH WHETHER YOU NEED USERNAME OR JUST PASSWORD
        username_input = self.driver.find_element(By.CSS_SELECTOR, 'input')
        username_input.send_keys(TWITTER_USERNAME)
        username_input.send_keys(Keys.ENTER)

        time.sleep(1)

        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"')
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        time.sleep(2)

        create_post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        create_post.click()

        time.sleep(1)

        text_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
        text_box.send_keys(f"My Internet Download Speed is {self.down} and Upload is {self.up}")
        time.sleep(2)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/button[2]')
        post_button.click()


bot = TwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
