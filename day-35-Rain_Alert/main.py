import requests
import os


API_KEY = os.environ["API_KEY"]                             #SAVED THE API KEY IN ENV VARIABLES FOR SAFETY:
print(API_KEY)                                              #RUN -> EDIT CONFIG -> EDIT CONFIG TEMPLATES -> PYTHON -> CHOOSE THE RIGHT FILE -> ADD ENV VARIABLE
#print(os.environ)

LONG = 51.5066
LAT = 0.3383

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt" : 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

#print(weather_data["list"][0]["weather"][0]["id"])              #GETS SINGLE WEATHER ID OF WANTED TIMESTAMP


will_rain = False

for item in weather_data["list"]:
    if item["weather"][0]["id"] <700:                           #Can't setup a twilio account without verifying with ID so it's annyoing
        will_rain = True

if will_rain:
    print("Bring an umbrella")



