import requests


# ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"
#
# response = requests.get(url=ISS_ENDPOINT)       #gets your response code 200
# #print(response.content)                         #response.content gets you the data you wanted
# data = response.json()                           #grabs data in json format
# #print(data["iss_position"]["longitude"])
#
# #response.raise_for_status()                    #if you don't get code 200, you'll get a specific exception
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (latitude, longitude)


#response codes meanings:
#1XX            "wait, processing"
#2XX            "Here you go"
#3XX            "No permission"
#4XX            "You screwed up, e.g 404 - whatever you're looking for doesn't exist"
#5XX            "Server screwed up"
#https://www.webfx.com/web-development/glossary/http-status-codes/


SUNSRISE_ENDPOINT = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat" : 51.507630,
    "lng" : -0.337460,
    "formatted" : 0,
}

response = requests.get(url=SUNSRISE_ENDPOINT, params=parameters)           #params=  lets you add necessary parameters
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise, "\n", sunset)

print(sunrise.split("T")[1].split(":")[0])      #formats time into an hour
