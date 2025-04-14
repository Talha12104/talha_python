
f = open("myfile.txt")
print(f.read())
f.close()

# Dont need to close the file
with open("myfile.txt") as f:
    print(f.read())