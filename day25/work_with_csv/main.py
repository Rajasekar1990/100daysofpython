# import csv

# Method 1 ###
# with open("weather_data.csv", "r") as csv_file:
#     content = csv_file.readlines()
#     print(content)
#
# mylist = []
# for item in content:
#     updated_content = item.strip("\n")
#     mylist.append(updated_content)
#     print(updated_content)

# method 2:
# with open("weather_data.csv", "r") as csv_data:
#     data = csv.reader(csv_data)
#     temperature = []
#     for item in data:
#         if item[1] != "temp":
#             temperature.append(int(item[1]))
#
# print(temperature)

import pandas

csv_data = pandas.read_csv("weather_data.csv")
# print(csv_data)
# print(f"{csv_data['temp']}")
#
# csv_dict = csv_data.to_dict()
# print(csv_dict)
#
# temperature_list = csv_data["temp"].to_list()
# print(temperature_list)

# # method 1
# nr = 0
# dr = 0
# for item in temperature_list:
#     dr += 1
#     nr += item
# avg = nr/dr
# print(int(round(avg, 2)))

# # method 2
# total = sum(temperature_list)
# count = len(temperature_list)
# avg = round(total / count)
# print(avg)

# method 3
# mean = csv_data["temp"].mean()
# print(round(mean))

# maximum = csv_data["temp"].max()
# print(maximum)

# # Get data in columns
# column_val = csv_data["condition"]
# print(column_val)
# # alternate way is:
# columns_val = csv_data.condition
# print(column_val)

# # Get a row val from the selected column
# row_val = csv_data[csv_data.day == "Monday"]
# print(row_val)

# # get the row for temp value is max
# max_temperature = csv_data[csv_data.temp == csv_data["temp"].max()]
# print(max_temperature)

# # get the weather condition for monday
# row_monday = csv_data[csv_data.day == "Monday"]
# print(row_monday)
# column_monday = row_monday.condition
# print(column_monday)
# temp_cel = row_monday.temp
# print(temp_cel)
# temp_farenheit = (temp_cel * (9/5)) + 32
# print(f"{temp_farenheit}")

# Create a data frame from pandas dataframe class
dict_frame = {
    "students": ["amy", "anderson", "clarke"],
    "marks": [70, 80, 90]
}

dict_data = pandas.DataFrame(dict_frame)
# print(dict_data)

# to write data frame into csv file
dict_data.to_csv("dict_data.csv")
print()

