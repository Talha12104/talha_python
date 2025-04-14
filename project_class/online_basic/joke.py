import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break and now it won't stop sending me Kit-Kat ads.",
    "Why did the programmer quit his job? Because he didn't get arrays."
]

user_input = input("What do you want? (type 'joke'): ").strip().lower()

if user_input == "joke":
    print(random.choice(jokes))
else:
    print("Sorry, I can tell only joke function")