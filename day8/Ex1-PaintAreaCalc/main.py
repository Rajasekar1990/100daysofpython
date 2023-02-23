print("Welcome to Paint Area Calculator.")
height = float(input("Enter Height of wall to paint in m "))
width = float(input("Enter Width of wall to paint in m "))
chargepercan = 5

def num_of_cans(h=height,w=width,c=chargepercan):
    cans=round((h*w)/c)
    print(f"You will need {cans} cans of paint.")

num_of_cans()