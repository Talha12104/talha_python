def madlibs():

    """
    This function generates a madlib story based on user input.
    """
    verb : str = input("Enter a verb: ")
    noun : str = input("Enter a noun: ")
    adjective: str = input("Enter an adjective: ")

    print(f"Once upon a time, {adjective} {noun} a decided to {verb} in the forest.")

if __name__ == "__main__":
    madlibs()

