a = int(input("Enter Your Age: "))
# if Statment No: 1 for First Condition
if(a>=18):
    print("You are above the age of consent")
    print("Good for you.")
elif(a<=0):
    print("Your Entering invalid age try again and put valid Information")
    a =int(input("Enter Your Correct Age: "))
# if Statment No: 2 for Negative Age input 
    if(a>=18):
        print("You are above the age of consent")
        print("Good for you.")
elif(a==0):
    print("You're Entering 0 which is not a valid Age")
    a = int(input("Enter your Correct Age: "))
    # if Statment No: 2 for Invalid Age input 
    if(a>=18):
        print("You are above the age of consent")
        print("Good for you.")

else: print("Your are below the age of consent")
print("Thank for using x,y,z Service")