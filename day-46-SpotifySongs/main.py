import spotipy
import requests
from bs4 import BeautifulSoup
from spotipy import SpotifyOAuth

TOP_SONGS_URL = "https://www.billboard.com/charts/hot-100/"

user_date = input("Please enter a date in the format 'YYYY-MM-DD': ")       #2014-06-07
url = TOP_SONGS_URL + str(user_date)

SPOTIFY_CLIENT_ID = os.environ.get["CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ.get["CLIENT_SECRET"]
SPOTIFY_REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
        username="chromosom")
)

print(url)

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=url, headers = header)
response.raise_for_status()
website_data = response.text

soup = BeautifulSoup(website_data, features="html.parser")

title_data = soup.find_all(name="h3", id="title-of-a-story")     

titles = []
for title in title_data:
    current_title = title.getText()
    titles.append(current_title.strip())

to_remove = ["Songwriter(s):", "Producer(s):", "Imprint/Promotion Label:", "Gains in Weekly Performance", "Additional Awards"]

titles = [item for item in titles if item not in to_remove]

print(titles)

user_id = sp.current_user()["id"]

song_uris = []
split_date = user_date.split("-")
for song in titles:
    result = sp.search(q=f"track:{song} year:{split_date[0]}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
