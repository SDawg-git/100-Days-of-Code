import requests

parameters = {
    "amount":   20,
    "type":    "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()


data = response.json()
#print(data["results"])
question_data = data["results"]
#print(question_data)





