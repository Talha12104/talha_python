def main():
    print("This program use to convert temperature from Celsius to Fahrenheit")
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"The temperature in Fahrenheit is {celsius}")

if __name__ == "__main__":
    main()