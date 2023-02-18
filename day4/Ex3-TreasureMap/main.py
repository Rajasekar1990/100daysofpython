print("Welcome To Treasure Map")
row1 = ["*","*","*"]
row2 = ["*","*","*"]
row3 = ["*","*","*"]

map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
pos=input("Pick a position from to place your treasure ")
print(pos)

rowpos=int(pos[0])
colpos=int(pos[1])

pickedelement=map[rowpos-1]
pickedelement[colpos-1] = "X"

print(f"{row1}\n{row2}\n{row3}")