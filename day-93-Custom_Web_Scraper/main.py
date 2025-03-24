from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

website_url = "https://steamdb.info"
driver = webdriver.Chrome(service=service)      # had to use a driver as the webpage JavaScript was not rendering
driver.get(website_url)



response = requests.get(url=website_url)
webpage = response.text

soup = BeautifulSoup(driver.page_source, "html.parser")

games_info = soup.find_all(class_="css-truncate")
print(games_info)

#since css-truncate contained all the titles on the page, I've decided to manually cut off the loop after 15 games
#as that's the maximum of games that are shown at once

count = 15
with open ("most_played_games.csv", "w") as file:

    for game_title in games_info:
        if count > 0:
            try:
                file.write(game_title.get_text(strip=True))
                file.write("\n")
                count-=1
            except(UnicodeError):   #russian titles caused unicode error so they will be skipped
                count-=1
