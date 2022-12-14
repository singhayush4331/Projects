import requests
from datetime import datetime
import smtplib as sl

MY_LONG = 86.425957 # Your longitude
MY_LAT = 23.794149 # Your latitude

# MY_LAT = -15 # Your latitude
# MY_LONG = -160 # Your longitude

gmail = "mayankpython9@gmail.com"
password = "python19"
receiver = "innovativecreations195@gmail.com"

def send_mail():
    with sl.SMTP("smtp.gmail.com") as c:
        c.starttls()
        c.login(user=gmail, password=password)
        c.sendmail(from_addr=gmail, to_addrs=receiver, msg="nacho")

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
now_hr = time_now.hour
# now_hr = 10

lat_diff = MY_LAT - iss_latitude
long_diff = MY_LONG - iss_longitude

print(sunset)
print(iss_longitude)
print(now_hr)
print(lat_diff, long_diff)

if 5 > lat_diff > -5 and -5 < long_diff < 5:
    if now_hr > sunset or now_hr < sunrise:
        send_mail()
        print("nacho")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



