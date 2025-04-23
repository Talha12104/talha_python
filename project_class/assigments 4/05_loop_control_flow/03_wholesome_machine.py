AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following {AFFIRMATION}")

    user_feedback = input()
    while user_feedback != AFFIRMATION:
        print("Please Enter the correct AFFIRMATION")
        user_feedback = input()
    print("That's rigth...")

if __name__ == "__main__":
    main()