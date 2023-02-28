from art import logo
import os

print("\nWelcome to the secret auction program.")
print(logo)

secret_auction={}

def play_auction (auctioner_name, auctioner_amount):
    secret_auction[auctioner_name]=auctioner_amount
    #print(secret_auction)

def auction_winner ():
    highest_bid=0
    new_player_name=""
    for player_name in secret_auction:
        new_highest_bid = secret_auction[player_name] 
        if (new_highest_bid >= highest_bid):
            highest_bid = new_highest_bid
            new_player_name = player_name
    
    print(f"The winner is {new_player_name} with a bid of ${highest_bid}")
        
checkflag=True
while checkflag:
    name=input("What is your name?: ")
    amount=int(input("What's your bid?: $"))
    result=(input("Are there any other bidders? Type 'yes' or 'no'.\n").lower())
    play_auction(name,amount)

    if (result == "yes"):
        os.system('clear')
        print("Welcome to the secret auction program.")
        print(logo)
        checkflag=True  
    elif (result == "no"):
        checkflag=False
        auction_winner()



