import random,os
from logo import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(player_card):
    if sum(player_card) == 21 and len(player_card) == 2:
        return 0
    if 11 in player_card and sum(player_card) > 21:
        player_card.remove(11)
        player_card.append(1)
    return sum(player_card)

def compare(final_user_score, final_computer_score):
    if (final_user_score == final_computer_score):
        return "Its a draw"
    elif (final_user_score == 0):
        return "You Win with a black jack"
    elif (final_computer_score == 0):
        return "You Lose, Computer has black jack"
    elif (final_user_score > 21):
        return (f"You Lose, user score is {final_user_score} > 21")
    elif (final_computer_score > 21):
        return (f"You Win, computer score is {final_computer_score} > 21")
    elif (final_user_score > final_computer_score):
        return (f"You Win, user score is {final_user_score} > computer score {final_user_score}")
    else:
        return (f"You Lose, computer score is {final_computer_score} > user score {final_user_score}")

def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    game_over_flag=False

    for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

    while not game_over_flag:
        user_score=calculate_score(player_card=user_cards)
        computer_score=calculate_score(player_card=computer_cards) 
        print(f"user cards are {user_cards}, user_score is: {sum(user_cards)}")
        print(f"computer's first card is: {computer_cards[0]}")

        if (user_score == 0 or computer_score == 0 or user_score > 21):
            game_over_flag=True
        else:
            check=input("does the user wants to draw another card? Type 'y' else 'n' ").lower()
            if check=="y":
                user_cards.append(deal_card())
                game_over_flag=False
            else:
                game_over_flag=True

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(player_card=computer_cards) 
        #print(f"computer cards are {computer_cards}, computer_score is: {sum(computer_cards)}")
        
    print(f"user cards are {user_cards}, user_score is: {sum(user_cards)}")
    print(f"computer cards are {computer_cards}, computer_score is: {sum(computer_cards)}")
    print(compare(user_score,computer_score))


while input("Do you want to play blackJack game? Type 'y' else 'n' ").lower():
    os.system('clear')
    play_game()