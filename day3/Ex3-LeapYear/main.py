year=int(input("Which year do you want to check? "))

flag=0
if ((year % 4) == 0):
    flag=1
    if ((year % 100) == 0):
        if ((year % 400) == 0):
            flag=1
        else:
            flag=0
    else:
        flag=1
else:
    flag=0

if (flag == 1):
    print(f"{year} is a leap year")
elif (flag == 0):
    print(f"{year} is not a leap year")
else:
    print()