import requests
from datetime import datetime


USERNAME = "innomayank"
TOKEN = "fhjkfsdgfkshrf9o"
GRAPH_ID = "g1"

today = datetime.now()
formatted_time = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# r = requests.post(url=pixela_endpoint, json=param)
# print(r.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_data = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "KM",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# r = requests.post(url=graph_endpoint, json=graph_data, headers=headers)
# print(r.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": formatted_time,
    "quantity": "21.0",
}
#
# r = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(r.text)
#

update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_time}"
updated_data = {
    "quantity": "5.5"
}

p = requests.put(url=update_pixel, json=updated_data, headers=headers)

print(p.text)

