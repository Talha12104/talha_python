import random

computer = random.choice([1, -1, 0])

youDict = {1: 1, 2: -1, 3: 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

try:
    you_num = int(input("Enter Your Choice (1: Snake, 2: Water, 3: Gun): "))
    if you_num not in youDict:
        raise ValueError("Invalid choice! Please choose 1, 2, or 3.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

you = youDict[you_num]

print(f"You Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

if you == computer:
    print("It's a Draw")
else:
    if (computer == -1 and you == 1):
        print("You Win")
    elif (computer == -1 and you == 0):
        print("You Lose")
    elif (computer == 1 and you == -1):
        print("You Lose")
    elif (computer == 1 and you == 0):
        print("You Win")
    elif (computer == 0 and you == -1):
        print("You Win")
    elif (computer == 0 and you == 1):
        print("You Lose")
    else:
        print("Something went wrong")
