enough_height = 168.7

def main():
    tall: float = float(input("Enter your Height (How tall are you): "))

    if tall >= enough_height:
        print("Your'e tall enough to ride")
    else:
        print("Your'e not tall enough but maybe next year")

if __name__ == "__main__":
    main() 

