from colorama import init, Fore, Style

def get_user_number():
    """
    Creating an empty list.
    Ask the user to put number in the list.
    Once they break a line, Break out of the loop and return the list"""

    user_number = []

    while True:
        user_input = input(f"{Fore.BLUE}Enter a number: ")

        if user_input == "":
            break

        num = int(user_input)
        user_number.append(num)
    return user_number



def count_nums(num_lst):
    """
    Creating a empty dictionary
    Loop over the list of numbers.
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in dictionary, increment its value by 1."""

    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    return num_dict

def print_count(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        print(f"{Fore.RED}{str(num)} appers {str(num_dict[num])} times.")

def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of time each number appeared in the list.
    """

    user_number = get_user_number()
    num_dict = count_nums(user_number)
    print_count(num_dict)

if __name__ == "__main__":
    main()
