print("Welcome to FizzBuzz")
userinput=int(input("Enter the range of the numbers "))

count=0
for i in range (1, userinput+1):
    if (i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
    count+=1

print(count)