import requests as rq
import os

# key = "bbc186e6f89739be484947f5c6a176da"
city = "dhanbad"
key = os.environ.get("KEY")
print(key)
# lat = 23.794149
# lon = 86.425957
lat = 15.619620
lon = 77.271347

link_open_call = "https://api.openweathermap.org/data/2.5/onecall"

one_call_param = {
    "lat":lat,
    "lon":lon,
    "appid":key,
    "exclude":"daily,minutely,current"
}

# r = rq.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}")

one_call = rq.get(url=link_open_call, params=one_call_param)

json_data = one_call.json()
print(json_data)
# for hourly in json_data["hourly"][:12]:
#     climate = hourly["weather"][0]
#     if climate["id"] < 700:
#         print("Bring an Umbrella")
        # break




