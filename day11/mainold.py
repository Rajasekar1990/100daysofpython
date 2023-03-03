import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

user_cards=[]
computer_cards=[]

def user_card_fn():
    user_cards.append(deal_card())
    return user_cards

def computer_card_fn():
    computer_cards.append(deal_card())
    return computer_cards

def calculate_score(player):
    user_total=0
    computer_total=0
    if (player == "user"):
        if (len(user_cards) <= 2):
            for i in range(0,2):
                user_card_drawn=user_card_fn()
                #print(user_card_drawn)
                user_total+=user_card_drawn[i] 
            return user_total
        else:
            user_card_drawn=user_card_fn()
            user_total+=user_card_drawn[len(user_cards)-1] 
            return user_total

    if (player == "computer"):
        if (len(user_cards) <= 2):
            for j in range(0,2):
                computer_card_drawn=computer_card_fn()
                #print(computer_card_drawn)
                computer_total+=computer_card_drawn[j]
            return computer_total
        else:
            computer_card_drawn=computer_card_fn()
            computer_total+=computer_card_drawn[len(computer_cards)-1] 
            return computer_total
                    
play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if (play == "y"):
    userscore=calculate_score(player="user")
    print(f"user score is : {userscore}")
    computerscore=calculate_score(player="computer")
    print(f"computer score is : {computerscore}")
    blackjack=21
    if (userscore == blackjack and computerscore == blackjack):
        print("draw")
    elif (userscore == blackjack):
        print(f"You Win")
    elif (computerscore ==  blackjack):
        print(f"You Lose")
    else:
        check=input("does user wants to draw a card Type 'yes' or 'no' ").lower()
        if (check=="yes"):
            userscore=calculate_score(player="user")
        
    if (userscore > 21):
        for k in user_cards:
            if k == 11:
                userscore-=10
                if (userscore > 21):
                    print("You Lose")
                elif (userscore < 21):
                    if (len(user_cards) > 2):
                        check=input("does user wants to draw a card Type 'yes' or 'no' ").lower()
                        if (check=="yes"):
                            userscore=calculate_score(player="user")
                        elif (check=="no"):  
                            computerscore=calculate_score(player="computer")
                            if (userscore == blackjack and computerscore == blackjack):
                                print("draw")
                            elif (userscore == blackjack):
                                print(f"You Win")
                            elif (computerscore ==  blackjack):
                                print(f"You Lose")
            else:
                print("You Lose")