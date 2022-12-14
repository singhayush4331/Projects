import requests

param = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

r = requests.get(url="https://opentdb.com/api.php", params=param)
# print(r.json())

question_data = r.json()["results"]

# print(question_data)