import requests
import datetime as dt
#HTTP REQUESTS
#GET        requests.get()  - ask for data
#POST       requests.post() - we give the data to the system, not interested in the response
#PUT        requests.put() - update a piece of data in an external service (e.g. spreadsheet)
#DELETE     requests.delete() - delete a piece of data

PIXELA_TOKEN = os.environ["PIXELA_TOKEN"]
PIXELA_USERNAME = os.environ["USERNAME"]

pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)      #PASSING PARAMS AS A JSON FILE
# print(response.text)                                        #ALREADY USED, CAN'T DO AGAIN AS PROFILE IS CREATED


graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
graph_params = {
    "id": "codingcourse",
    "name": "100 Days of Code",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint ,json=graph_params, headers=headers)
# print(response.text)                                                                          #already created graph


#ADDING A PIXEL

today_dt = str(dt.datetime.today())
today = today_dt.split()[0].replace("-", "")            #COULD'VE DONE IT USING strftime

GRAPH_ID = "codingcourse"
post_params = {
    "date": today,
    "quantity": "1",
}

# response = requests.post(url=f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}", headers=headers, json=post_params)
# print(response.text)


#UPDATING A PIXEL

update_params = {
    "quantity": "5",
}

# response = requests.put(url=f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/20241113", headers=headers, json=update_params)
# print(response.text)


#DELETE A PIXEL

response = requests.delete(url=f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/20241114", headers=headers)
print(response.text)



