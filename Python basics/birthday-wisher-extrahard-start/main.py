import datetime as dt
import random as r
import pandas as p
import smtplib as sl


mail = "mayankpython9@gmail.com"
password = "python19"
# receiver = "innovativecreations195@gmail.com"
# receiver1 = "singhayush4331@gmail.com"

def send_mail():
    n = (r.randint(1, 3))
    with open(f"letter_templates/letter_{n}.txt", mode="r") as l:
        letter = l.readlines()
        a = letter[0].replace("[NAME]", birthdays[0]["name"])

    receiver = birthdays[0]["email"]
    body = ''.join(letter[1:])
    print(body)
    with sl.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(from_addr=mail,
                            to_addrs=receiver,
                            msg=f"Subject:Surprise\n\n {a}{body}")


csv_data = p.read_csv("birthdays.csv")
birthdays = csv_data.to_dict(orient="records")

now = dt.datetime.now()
day = now.day
month = now.month

print(birthdays[0]["month"])

if day == birthdays[0]["day"] and month == birthdays[0]["month"]:
    send_mail()



##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




