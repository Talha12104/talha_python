def main(n):
    if (n==1 or n==0):
        return 1
    return n + n

n = int(input("Enter your number: "))
print(f"The factorial number of your input is {main(n)}")
while n < 100:
    n = main(n)
    print(f"After doubling, your number is now {n}")