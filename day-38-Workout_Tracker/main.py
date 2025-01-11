import requests
import datetime as dt

NUTRI_API_KEY = os.environ["NUTRI_API"]
NUTRI_APP_ID = os.environ["NUTRI_ID"]
NUTRI_APP_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/7a932061aa86b6618097f84ba3bd8ece/myWorkouts/workouts"
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

GENDER = "Male"
WEIGHT_KG = 80
HEIGHT_CM = 192
AGE = 22


nutri_headers = {
    "x-app-key": NUTRI_API_KEY,
    "x-app-id": NUTRI_APP_ID,
}


user_query = input("Please describe what you have done today: ")

nutri_query = {
    "query": user_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=NUTRI_APP_ENDPOINT, headers=nutri_headers, json=nutri_query)
response.raise_for_status()
data = response.json()


date = str(dt.datetime.now().date().strftime("%d/%m/%Y"))
time = str(dt.datetime.now().time().strftime("%X"))


exercise = data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

exercise_data = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}

print(exercise_data)

sheety_headers = {
    "Authorization": os.environ["BEARER"]
}

sheety_post = requests.post(url=SHEETY_ENDPOINT, json=exercise_data, headers=sheety_headers)
sheety_post.raise_for_status()
sheety_data = sheety_post.json()
