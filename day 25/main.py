# # list = []
#
# with open("weather_data.csv") as l:
#     lit = l.readlines()
#     print(lit)
#

# import csv
#
# temp = []
#
# with open("weather_data.csv") as l:
#     data = csv.reader(l)
#     for i in data:
#         if i[1] != "temp":
#             print(type(i[1]))
#             temp.append(int(i[1]))
#     print(temp)
#
#
# import pandas
#
# csv_data = pandas.read_csv("weather_data.csv")
#
# # print(csv_data["temp"])
# #
# # data_list = csv_data["temp"].to_list()
# # print(data_list)
# # total = 0
# # no_of_data = 0
# # for i in data_list:
# #     total += i
# #     no_of_data += 1
# # print(int(total / no_of_data))
#
# # average = sum(data_list) / len(data_list)
# #
# # max_temp = csv_data["temp"].max()
# #
# # print(max_temp)
# # print(csv_data[csv_data.temp == max_temp])
# # print(int(average))
#
#
# monday = csv_data[csv_data.day == "Monday"]
# m_temp = monday.temp
# in_fahreinheit = (m_temp * 9/5) + 32
# print(in_fahreinheit)



import pandas

all_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(all_data["Primary Fur Color"])
fur = all_data["Primary Fur Color"]


gray_color = fur[fur == "Gray"]
black_color = fur[fur == "Black"]
cinnamon_color = fur[fur == "Cinnamon"]
print(gray_color)
gray_no = len(gray_color)
black_no = len(black_color)
cinnamon_no = len(cinnamon_color)

data = {
    "Fur colour" : ["Gray", "Black", "Cinnamon"],
    "No" : [gray_no, black_no, cinnamon_no]
}

dic = pandas.DataFrame(data)
dic.to_csv("Nacho.csv")

print(data)

# data = pandas.DataFrame(dict)
#
# print(data)


















