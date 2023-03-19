from prettytable import PrettyTable

# from turtle import *
# my_obj = Turtle()
# print(my_obj)
# my_obj.shape("turtle")
# my_obj.color("blue")
# my_obj.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick

table_obj = PrettyTable()
#print(table_obj)

table_obj.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table_obj.add_column("Type", ["Electric", "Water", "Fire"])
# table_obj.align["Pokemon"] = "l"
# table_obj.align["Type"] = "l"
table_obj.align = "l"
print(table_obj)

table1 = PrettyTable()
table1.field_names = ["Pokemon", "Type"]
table1.add_row(["Pikachu", "Electric"])
table1.add_row(["Charmandar", "Fire"])
table1.align = "l"
print(table1)


