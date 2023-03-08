import random
from logo import logo
from game_data import data
print(logo)
# print(dict_picked["follower_count"])
def pick_dictionary (dict_lib):
    dict_picked=(data[random.randint(0,len(data)-1)])
    return dict_picked

new_dict_list=[]
new_dict={}

for i in range(2):
    dict=pick_dictionary(data)
    for items in dict:
        new_dict["name"]=dict["name"]
        new_dict["description"]=dict["description"]
        new_dict["country"]=dict["country"]
    new_dict_list.append(new_dict)
    
    
print(new_dict_list)


# def random_dict (dict):
#     compare=f'{dict["name"]}, {dict["description"]}, {dict["country"]}'
#     return compare

# random_dict(dict_picked)

#compare1=print(f"Compare A: {random_dict(dict_picked)}")
#compare2=print(f"Against B: {random_dict(dict_picked)}")

#user_answer=input("Who has more followers? Type 'A' or 'B': ")



