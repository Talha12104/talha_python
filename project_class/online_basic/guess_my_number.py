import random

def main():
    number = random.randint(1, 100)
    print("I am thinking a number between 1 to 99")
    while True:
        num = int(input("Enter your guess: "))
        if num < number:
            print("Your guess is too low.")
            print("")
        elif num > number:
            print("Your guess is too high.")
            print("")
        else:
            print(f"Congrats. You guessed the right number: {number}.")
            break

if __name__ == "__main__":
    main()