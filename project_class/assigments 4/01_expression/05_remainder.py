def main():
    dividend : int = int(input("Please enter an integer to be dividend: "))
    divisor : int = int(input("Please enter an integer to be divisor: "))

    quotient : int = dividend // divisor
    remainder : int = dividend % divisor

    print(f"The result of this division is {str(quotient)} with the remainder of {remainder}")

if __name__ == '__main__':
    main() 