import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

GENDER = "male"
WEIGTH_KG = 74
HEIGHT_CM = 152.4 + 19.05
AGE = 15

USERNAME = "may"
PASS = "pass"

ID = "7f9a31b9"
KEY = "7e169876c194b23b254afc48f7294430"

trackapi_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/b79a6cda368e8b10aed58d6970796335/myWorkouts/workouts"


query = input("Tell me which exercises you did: ")

param = {
    "query": query,
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGTH_KG,
    "height_cm": HEIGHT_CM
}

headers = {
    "x-app-id": ID,
    "x-app-key": KEY
}


r = requests.post(url=trackapi_endpoint, json=param, headers=headers)

print(r.json())


date = datetime.now().strftime("%x")
time = datetime.now().strftime("%X")
print(date)
print(time)

da = r.json()
for exercise in da["exercises"]:
    data = {

    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise['name'].title(),
        "duration": exercise['duration_min'],
        "calories": exercise['nf_calories'],
        }
    }
    s = requests.post(sheety_endpoint, json=data, auth=HTTPBasicAuth(USERNAME,PASS))
    print(s.text)



