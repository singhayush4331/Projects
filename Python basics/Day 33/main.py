# import requests
#
# r = requests.get(url="http://api.open-notify.org/iss-now.json")
# r.raise_for_status()
# d = r.json()
#
# print(d)
#
import requests
import datetime as dt

now = dt.datetime.now()
now_time = now.time()

LAT = 23.794149
LNG = 86.425957

parameters = {
    "lat" : LAT,
    "lng" : LNG,
    "formatted": 0
}

r = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
r.raise_for_status()
d = r.json()

sunrise = d["results"]["sunrise"]

sunrise_hr = sunrise.split("T")[1].split(":")[0]

print(sunrise_hr, now_time)


