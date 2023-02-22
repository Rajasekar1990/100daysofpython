import random

from game_img import logo
print(f"{logo}\n")

from game_img import stages

from dictionary import word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word= (random.choice(word_list)).lower()


display=[]
for j in random_word:
    display.append("_")
# print(f"{display}\n")

flag = False
lives = 6

while not flag:
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    userinput= input("Guess a letter: ").lower()
    
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for i in range(len(random_word)):
        k = random_word[i]
        #print(f"Current position: {i}\n Current letter: {k}\n Guessed letter: {userinput}")
        if (k == userinput):
            display[i]=k
    # print(f"\n{display}\n")
    
    print(f"{' '.join(display)}\n")

    if userinput not in random_word:
        lives -= 1
        print(f"lives: {lives}\n")
        if (lives == 0):
            flag = True
            print("You Lose!")
            print(f"\nrandom word chosen from the list is {random_word}")

    if "_" not in display:
        flag = True
        print("You Win!")

    print(stages[lives]+"\n")