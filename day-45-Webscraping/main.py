import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

titles = soup.find_all(class_="title")
titles.reverse()

countdown = 100
for movie in titles:
    if countdown > 0 :
        movie_title = movie.getText()
        countdown-=1
        with open("movies.txt", "a", encoding="utf-8") as file:
            file.write(f"{movie_title}, \n")



