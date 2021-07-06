# import csv
#
# with open("./weather_data.csv") as data1:
#     data = csv.reader(data1)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
# print(temperature)

import pandas

data = pandas.read_csv("park.csv")
gray = data["Primary Fur Color"] == "Gray"
red = data["Primary Fur Color"] == "Cinnamon"
black = data["Primary Fur Color"] == "Black"
q, w, e = sum(gray), sum(red), sum(black)
print(gray)
#
# data_dict = {
#     "Fur Color": ["gray", "red", "black"],
#     "Count": [q, w, e]
# }
# data_frame = pandas.DataFrame(data_dict)
# data_frame.to_csv("squerral_count.csv")
# #
# y = data[data.temp == data.temp.max()]

# monday = data[data.day == "Monday"]
# far = monday.temp * 1.8 + 32

