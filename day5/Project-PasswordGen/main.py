import random

alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["!","@","#","$","%","^","&","*","(",")","_","+"]

print("Welcome to PyPassword Generator!")
lettersize=int(input("How many letters would like in your password?\n"))
symbolsize=int(input("How many symbols would you like?\n"))
numsize=int(input("How many numbers would you like?\n"))

#method 1:
symbolgenerated=""
numbergenerated=""
lettergenerated=""
temp1=""
temp2=""
temp3=""

for i in range(1,lettersize+1):
    lettergenerated=random.choice(alphabets)
    temp3+=lettergenerated
#    print(temp3)
for j in range(1,symbolsize+1):
    symbolgenerated=random.choice(symbols)
    temp1+=symbolgenerated
#    print(temp1)
for k in range(1,numsize+1):
    numbergenerated=random.choice(numbers)
    temp2+=numbergenerated
#    print(temp2)

finalpassword=temp3+temp1+temp2
print("Here is your password: "+finalpassword)

#method 2:  
password_list=[]

for l in range(1,lettersize+1):
    password_list.append(random.choice(alphabets))

for m in range(1,symbolsize+1):  
    password_list.append(random.choice(symbols))

for n in range(1,numsize+1):
    password_list.append(random.choice(numbers))

#print(password_list)
random.shuffle(password_list)
#print(password_list)

finalpassword1=""
for o in password_list:
    finalpassword1=finalpassword1+o

print("Here is your password: "+finalpassword1)