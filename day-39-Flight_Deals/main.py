import os
import datetime
import requests
from dotenv import load_dotenv


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    load_dotenv()


    def __init__(self):
        self.AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
        self.AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")
        self.AMADEUS_TOKEN = self.get_new_token()
        self.tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
        self.six_months = datetime.date.today() + datetime.timedelta(days = 6 * 30)




    def get_new_token(self):
        AMADEUS_TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"

        AMADEUS_HEADER = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        AMADEUS_BODY = {
            "grant_type": "client_credentials",
            "client_id": self.AMADEUS_API_KEY,
            "client_secret": self.AMADEUS_API_SECRET,
        }

        response = requests.post(url=AMADEUS_TOKEN_URL, headers=AMADEUS_HEADER, data=AMADEUS_BODY)
        response.raise_for_status()
        data = response.json()
        token = data["access_token"]
        print(token)
        return token





    def get_flights(self):

        AMADEUS_FLIGHTS_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        flight_request = {
            "originLocationCode": "LDN",
            "destinationLocationCode": "PAR",               #hardcode for now, change as an import later
            "departureDate": self.tomorrow,
            "returnDate": self.six_months,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        flight_headers = {"Authorization": f"Bearer {self.AMADEUS_TOKEN}"}




        response = requests.get(url=AMADEUS_FLIGHTS_URL, headers=flight_headers, params=flight_request)     #keep getting an error "Invalid HTTP header", i've checked a bajillion times
        response.raise_for_status()                                                                         #and still nothing
        available_flights = response.json()
        print(available_flights)
        print(flight_headers)


search = FlightSearch()
search.get_flights()
