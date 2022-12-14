







# import smtplib
# import datetime as dt
# import random as r
# mail = "mayankpython9@gmail.com"
# password = "python19"
# receiver = "innovativecreations195@gmail.com"
# receiver1 = "singhayush4331@gmail.com"
#
# #
#
# with open("quotes.txt", mode="r") as q:
#         quote = q.readlines()
#
#
# now = dt.datetime.now()
# day = now.weekday()
# if day == 4:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=mail, password=password)
#         connection.sendmail(from_addr=mail,
#                             to_addrs=receiver,
#                             msg=f"Subject: Quote of the day\n\n{r.choice(quote)}"
#                             )
#
# print(day)



