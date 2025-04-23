import random

def guess(x):
    random_number = random.randint(1, x)
    print("Welcome to the Guess the Number game!")
    guess = 0
    while guess != random_number:
        print(f"Guess a number between 1 and {x}")
        guess = int(input("Enter your guess: "))
        if guess < random_number:
            print("Your guess is to low")
        if guess > random_number:
            print("Your guess is to High.")
        if guess == random_number:
            print(f"Congrats you guess the right number {random_number}")

guess(100)