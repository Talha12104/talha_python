import random

num : int = 6

def main():

    die1 : int = random.randint(1, num)
    die2 : int = random.randint(1, num)

    total : int = die1 + die2

    print(f"Dice have {num} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total Dice = {total}")

if __name__ == '__main__':
    main()