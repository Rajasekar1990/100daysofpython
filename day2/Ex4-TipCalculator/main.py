print("Welcome to the tip calculator.")
billamt=input("what was the total bill? $")
tippercentage=input("What percentage tip would you like to give? 10, 12, or 15? ")
totalpersons=input("How many people to split the bill? ")

tipamt=round((float(billamt)*(int(1)+(float(tippercentage)/100)))/int(totalpersons),2)
tipamt_2decimals="{:.2f}".format(tipamt)

print(f"Each person should pay: ${tipamt_2decimals}")