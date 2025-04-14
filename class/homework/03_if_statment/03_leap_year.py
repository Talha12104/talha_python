def main():
    year: int = int(input("Enter you Year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"This Year {year} is a leap year.")
    else:
        print("Thats not the leap year.")

if __name__ == "__main__":
    main()
