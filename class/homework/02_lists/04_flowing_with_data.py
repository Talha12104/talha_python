def add_three_copies(mylist, data):
    for i in range(3):
        mylist.append(data)

def main():
    message = input("Enter the Message of copy: ")
    mylist = []
    print(f"List Before: {mylist}")
    add_three_copies(mylist, message)
    print(f"List After: {mylist}")

if __name__ == '__main__':
    main()