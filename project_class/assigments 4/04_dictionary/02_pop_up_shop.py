def main():
    fruits = {"Apple": 2, "Banana": 0.95, "Cherry": 0.75, "Date": 3.0, "Mango": 4.5}
    total_cost = 0

    print("Welcome to the Pop-Up Shop!")
    print("We have the following fruits available:")
    for fruit, price in fruits.items():
        print(f"{fruit}: ${price:.2f} each")

    for fruit_name, price in fruits.items():
        try:
            amount_bought = int(input(f"How many {fruit_name}s would you like to buy? "))
            if amount_bought <= 0:
                print("We appreciate your interest. Perhaps you'll make a purchase next time.")
                continue
            total_cost += amount_bought * price
        except ValueError:
            print("Please enter a valid number.")
            continue

    print(f"\nThank you for shopping with us! Your total cost is: ${total_cost:.2f}")

if _name_ == "_main_":
    main()