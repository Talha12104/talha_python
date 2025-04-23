import random

num = 6
def roll_dice():
    dice1 = random.randint(1, num)
    dice2 = random.randint(1, num)
    total : int = dice1 + dice2
    print(f"Total of two Dice: {total}")

def main():
    die1: int = 10
    print(f"Die in main start as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("Die in main end as: " + str(die1))


if __name__ == '__main__':
     main()

