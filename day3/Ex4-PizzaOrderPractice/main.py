print("Welcome to Python Pizza Deliveries!")
size=input("Which size Pizza do you want? S, M, or L ")
add_pepperoni=input("Do you want pepperoni? Y or N ")
extra_cheese=input("Do you want extra cheese? Y or N ")

finalbill=0

if(size=="S"):
    finalbill+=15
    if(add_pepperoni=="Y"):
        finalbill+=2
        if(extra_cheese=="Y"):
           finalbill+=1
elif(size=="M"):
    finalbill+=20
    if(add_pepperoni=="Y"):
        finalbill+=3
        if(extra_cheese=="Y"):
           finalbill+=1
elif(size=="L"):
    finalbill+=25
    if(add_pepperoni=="Y"):
        finalbill+=3
        if(extra_cheese=="Y"):
           finalbill+=1
else:
    finalbill
print(f"Your final bill is: ${finalbill}")
