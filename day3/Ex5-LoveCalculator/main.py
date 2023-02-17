print("Welcome to Love Calulator.")
name1=input("what is your first name? ")
name2=input("what is your second name? ")

name1_lowercase=name1.lower()
name2_lowercase=name2.lower()

check=name1+name2
part1=check.count("t")+check.count("r")+check.count("u")+check.count("e")
part2=check.count("l")+check.count("o")+check.count("v")+check.count("e")

score=str(part1)+str(part2)
score=int(score)

if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
if (score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")