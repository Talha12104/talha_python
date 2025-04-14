def main():

    Bangladesh: int = 16
    Pakistan: int = 18
    India: int = 20

    user_age: int = int(input("Enter your Age: "))

    if user_age >= Bangladesh:
        print(f"You can Vote in Bangladesh where the voting age is {Bangladesh}")

    else:
        print(f"You can't vote in Bangladesh where the voting age is {Bangladesh}")

    if user_age >= Pakistan:
        print(f"You can Vote in Pakistan where the voting age is {Pakistan}")

    else:
        print(f"You can't vote in Pakistan where the voting age is {Pakistan}")

    if user_age >= India:
        print(f"You can Vote in India where the voting age is {India}")

    else:
        print(f"You can't vote in India where the voting age is {India}")

if __name__ == "__main__":
    main()