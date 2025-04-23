import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # all uppercase letters
    used_letters = set()  # what the user has guessed
    lives = 6  # number of lives

    print("Welcome to Hangman!")
    print("You have 6 lives. Good luck!")

    # Main game loop
    while len(word_letters) > 0 and lives > 0:
        print("\nYou have used these letters: " + " ".join(sorted(used_letters)))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: " + " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Good guess!")
            else:
                lives -= 1
                print(f"Letter not in word. You have {lives} lives left.")
        elif user_letter in used_letters:
            print("You have already guessed that letter. Try again.")
        else:
            print("Invalid input. Please enter a valid letter.")

    # End game messages
    if lives == 0:
        print(f"\nYou lost! The word was {word}.")
    else:
        print(f"\nCongratulations! You guessed the word {word}!")

if __name__ == "__main__":
    hangman()
