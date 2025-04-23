import random

def main():
    for _ in range(10):
        random_number = random.randint(1, 100)
        print(random_number, end=" ")

if __name__ == "__main__":
    main()