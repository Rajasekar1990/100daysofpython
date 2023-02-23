print("Welcome to Prime Number Checker")

#num_to_check=int(input("Enter your number to check: "))
numrange=int(input("Enter the number: "))

#method:1
def primecheck (num):
    flag = True
    for i in range(2, num):
        if (num % i == 0):
            flag = False
    
    if (num == 1):
        print(f"{num} is neither a prime nor a composite number")
        #return 2
    elif (flag == True):
        print(f"{num} is a prime number")
        #return 1
    elif (flag == False):
        print(f"{num} is not a prime number")
        #return 0

#method:2
def primecheck1 (num):
    flag = True; i = 2
    while (flag == True and i < num):
        if num % i == 0:
            flag = False
        i+=1
    
    if (num == 1):
        #print(f"{num} is neither a prime nor a composite number")
        return 2
    elif (flag == True):
        #print(f"{num} is a prime number")
        return 1
    elif (flag == False):
        #print(f"{num} is not a prime number")
        return 0

#To check whether the given number is prime number
primecheck(numrange)

#To print the list of prime numbers from 1 to upto the given number
temp=""
for j in range(1, numrange+1):
    if (primecheck1(j) == 1):
        temp=temp+" "+f"{j}"
print("prime numbers present in the given range are:"+temp)


    