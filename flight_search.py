import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()
TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
CITY_SEARCH_ENDPOINT = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ['AM_API_KEY']
        self._api_secret = os.environ['AM_API_SECRET']
        self._token = self._get_new_token()
        self._auth = f'Bearer {self._token}'

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        header = {
            'Authorization': self._auth,
        }
        body = {
            'keyword': city_name
        }

        response = requests.get(url=CITY_SEARCH_ENDPOINT, headers=header, params=body)

        try:
            code = response.json()['data'][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}")
            return 'N/A'
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}")
            return 'Not found'

        return code
