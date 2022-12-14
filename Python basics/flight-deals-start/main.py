#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# import requests
# from pprint import pprint
#
# sheety_endpoint = "https://api.sheety.co/b79a6cda368e8b10aed58d6970796335/flightDeals/prices/2"
#
# r = requests.get(url=sheety_endpoint)
#
# # sheet_data = r.json()['prices']
# pprint(r.json())


from data_manager import DataManager

d = DataManager()

d.tequilo()