import requests
from pprint import pprint

sheety_endpoint = "https://api.sheety.co/b79a6cda368e8b10aed58d6970796335/flightDeals/prices/"

KIWI_API = "IBNWm1biqUThxEZDhPtqCJg8XFx8rtOX"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/"

headers = {
    'apikey': KIWI_API
}

data = {
    'price': {
        'iataCode': "TESTING"
    }
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        r = requests.get(url=sheety_endpoint)
        self.sheet_data = r.json()['prices']

    def update_data(self):
        for i in range(2, 11):
            r = requests.put(url=f"{sheety_endpoint}{i}", json=data)
            pprint(r.json())

    def tequilo(self):
        query = {
            'term': "Paris",
            'location_types': "city"
        }
        r = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=headers, params=query)
        print(r)
