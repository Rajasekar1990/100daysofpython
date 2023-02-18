import random
print("Welcome to Banker Roulette.")
mylist=input("enter the set of name with comma seperated: ")
print(mylist)
mylist_delimited=mylist.split(",")
print(mylist_delimited)
count=len(mylist_delimited)
#print(count)
randomno=random.randint(0,(count-1))
#print(randomno)
randomname=mylist_delimited[randomno]
print(f"{randomname} is going to buy the meal today!")