import random 
from logo import logo
import os
os.system('clear')
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num_picked=random.randint(1,100)
print(f"Pssst, the correct answer is {num_picked}")

def easy (user_guess):
        if(user_guess > num_picked):
            print("Too High")
        elif(user_guess < num_picked):
            print("Too Low")
        elif(user_guess == num_picked):
            print(f"You got it! The answer was {user_guess}")
            return 0
        
def hard (user_guess):    
        if(user_guess > num_picked):
            print("Too High")
        elif(user_guess < num_picked):
            print("Too Low")
        elif(user_guess == num_picked):
            print(f"You got it! The answer was {user_guess}")
            return 0

def play():
    diff_level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if (diff_level == "easy"):
        chances=10
    elif(diff_level == "hard"):
        chances=5
    while chances != 0:
        if (diff_level == "easy"):
            print(f"You have {chances} attempts remaining to guess the number") 
            guess_num=int(input("Make a guess: "))
            ret_val=easy(guess_num)
        elif (diff_level == "hard"):
            print(f"You have {chances} attempts remaining to guess the number") 
            guess_num=int(input("Make a guess: "))
            ret_val=hard(guess_num)     
        if (ret_val == 0):
                chances=0
        else:
            chances=chances-1
            if (chances >= 1):
                print("Guess Again")
    if (ret_val !=0):
        print("You've run out of guesses, you lose.")

play()