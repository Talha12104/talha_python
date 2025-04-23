def read_phone_number():
    phonebook = {}
    return phonebook

def add_number(phonebook):
    while True:
        name = input("Enter name: ")
        if name == "":
            break
        phone_number = input("Enter phone number: ")
        phonebook[name] = phone_number
        print(f"Added {name}: {phone_number}")

def remove_number(phonebook):
    name = input("Enter name to remove: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Removed {name}")
    else:
        print("Name not found")

def print_phone_number(phonebook):
    if not phonebook:
        print("Phonebook is empty.")
    else:
        for name, phone_number in phonebook.items():
            print(f"{name}: {phone_number}")

def lookup_number(phonebook):
    name = input("Enter name to look up: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("Not found")

def main():
    phonebook = read_phone_number()
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Number")
        print("2. Remove Number")
        print("3. Lookup Number")
        print("4. Print Phonebook")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_number(phonebook)
        elif choice == "2":
            remove_number(phonebook)
        elif choice == "3":
            lookup_number(phonebook)
        elif choice == "4":
            print_phone_number(phonebook)
        elif choice == "5":
            print("Exiting phonebook.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()