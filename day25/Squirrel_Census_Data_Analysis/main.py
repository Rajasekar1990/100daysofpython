import pandas

# To get the data of primary fur color of squirrel from squirrel data and create a csv with count of squirrels
# for each color
squirrel_data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrels_ct = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_ct = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_ct = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(f"{gray_squirrels_ct}, {red_squirrels_ct}, {black_squirrels_ct}")

data_dict = {
    "Fur_Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_ct, red_squirrels_ct, black_squirrels_ct]
}

csv_file = pandas.DataFrame(data_dict)
csv_file.to_csv("squirrel_ct.csv")


# Kodekloud PCEP Mock Test 1 to 5
# matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
#
# matrix2 = []
#
# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)
#
# print(matrix2[2][0])

# matrix = [[j for j in range(3)] for i in range(3)]
# print(matrix)
# print(matrix[1][2])
# del matrix[1]
# print(matrix)
#
# i = 5
# while True:
#     if i%0o11 == 0:
#         break
#     print(i)
#     i += 1
#
# print(bool(1))
#
# list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
# print(list1[2].upper())

# mylist = ([[j for j in range(4)] for i in range(4)])
# print(mylist[3][1])


# x = (3,)
# print(x[0])
#
# matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
#
# for i in matrix:
#     for j in i:
#         print(j)

# m = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
# print(m)
# print(m[1][1][1])

# list1 = [1,2,3,4]
# for i, j in enumerate(list1):
#     print(i, j)

# my_list = [4, 5, 6, 7, 8]
# print(my_list.index(7))

# def multi_num(num):
#     return int(input()) * num
#
#
# print(multi_num(num=5))

# matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
#
# matrix2 = []
#
# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)
#
# print(matrix2)

# def my_function(arg1, *argv):
#     print ("First argument:", arg1)
#     for arg in argv:
#         print("Next argument:", arg)
#
# my_function('Welcome', 'to', "python", "Raj!")

# list1 = [4, 4, 3, 1]
# list1.pop(1)
# print(list1)

# list1=["Go","Java","C","Python", "asdfiuhewrakfn"]
# print(max(list1))

# list1 = [0, 3, 4, 1, 2]
# list1[2:5]=[8,9]
# print(list1)

# list1 = [10, 11, 12, 13, 14]
# print(list1[::-1])
#
# tuple1 = 1,2,3,4,5
# print(tuple1)
#
# print(result1)


# matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
# print(matrix)
#
# countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
# countries2  = [country for sublist in countries for country in sublist if len(country) < 6 ]
#
# print(countries2)
#
# a = []
# for i in range(5):
#     a.append([])
#     for j in range(5):
#         a[i].append(j)
#
# print(a)

# x = 'abcd'
# u = x.upper()
# print(x, u)
#
# list1=[7,8,1,3,9]
# list1.remove(9)
# print(list1)
# # print(sum(list1))
#
# x = 0
# while (x < 50):
#   x+=2
#
# print(x)
#
# y = 20
# x = y += 3
# print(x)