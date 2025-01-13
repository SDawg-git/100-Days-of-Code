import os
from urllib.parse import quote

import requests
from pprint import pprint
from dotenv import load_dotenv

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    load_dotenv()

    def __init__(self):


        self.SHEETY_URL = os.getenv("SHEETY_URL")
        self.SHEETY_HEADER = {
            "Authorization": os.getenv("SHEETY_AUTH")
        }


        self.destination_data = {}



    def get_prices(self):

        response = requests.get(url=self.SHEETY_URL, headers=self.SHEETY_HEADER)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data





DataManager().get_prices()
