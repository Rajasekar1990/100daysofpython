import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images=[rock,paper,scissors]

yourchoice=input("what do you choose? Type 0 for Rock, 1 for paper or 2 for scissors\n")
yourchoice=int(yourchoice)
if(yourchoice < 0 or yourchoice > 2):
    print("you have chosen an invalid numnber. plesae try again")
else:
    print(images[yourchoice])
    computerchoice=random.randint(0,2)
   
    print("Computer chose:")
    print(images[computerchoice])
   
    if(yourchoice == computerchoice):
        print("its a draw")
    elif(yourchoice == 1 and computerchoice == 2):
        print("You Lose!")
    elif(yourchoice == 1 and computerchoice == 0):
        print("You Lose!")
    elif(computerchoice == 1 and yourchoice == 2):
        print("You Win!")
    elif(computerchoice == 1 and yourchoice == 0):
        print("You Win!")
    else:
        print("You Lose!")