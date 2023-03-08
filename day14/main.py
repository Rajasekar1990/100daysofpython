import random
from logo import logo,vs
from game_data import data
import os

def format_account (account):
    account_name=account["name"]
    account_description=account["description"]
    account_country=account["country"]
    formatted_string=f"{account_name}, a {account_description}, from {account_country}"
    return formatted_string

def verify_answer(user_answer, follower_ct_a, follower_ct_b):
    if follower_ct_a > follower_ct_b:
        return user_answer == "A"
    else:
        return user_answer == "B"

def game():
    #constants
    score=0
    continue_flag=True
    
    #display the logo
    print(logo)
    
    #get a random data from dictionary "data" for A and B
    account_a=random.choice(data)
    account_b=random.choice(data)
    # check if account_a and account_b is same if same get a different account for account_b
    while (account_a == account_b):
        account_b=data[random.randint(0, len(data)-1)]

    while continue_flag:
        account_a=account_b
        account_b=random.choice(data)
        while (account_a == account_b):
            account_b=data[random.randint(0, len(data)-1)]
        
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        user_input=input("Who has more followers? Type 'A' or 'B': ").upper()
        a_follower_count=account_a["follower_count"]
        b_follower_count=account_b["follower_count"]
        result=verify_answer(user_input,a_follower_count,b_follower_count)

        os.system('clear')
        print(logo)
        if result:
            score+=1
            print(f"Correct! Current score: {score}.")
        else:
            print(f"Incorrect answer, game over and You final score is: {score}")
            continue_flag=False

game()