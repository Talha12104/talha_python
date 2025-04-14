sentence_start : str = ("Karachi is the fun place. I used to live here to see")

def main():
    adjective : str = str(input("Please type an adjective and press enter: "))
    noun : str = str(input("Please type an noun and press enter: "))
    verb : str = str(input("Please type an verb and press enter: "))

    print(f"{sentence_start} {adjective} {noun} {verb}.")

if __name__ == '__main__':
    main()