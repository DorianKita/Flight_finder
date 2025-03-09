from dotenv import load_dotenv
import os
import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

load_dotenv()
SHEETY_ENDPOINT= 'https://api.sheety.co/de9862cff422df325716dc388558dc1d/flightDeals/prices'

class DataManager:

    def __init__(self):
        self._username = os.environ['SHEETY_USERNAME']
        self._password = os.environ['SHEETY_PASSWORD']
        self.authorization = HTTPBasicAuth(username=self._username, password=self._password)


    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self.authorization)
        sheet_data = response.json()['prices']
        return sheet_data

