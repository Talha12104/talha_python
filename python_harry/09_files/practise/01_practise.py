f = open("file.txt")

lines = f.readlines()
# print(lines)

for line in lines:
    if "Twinkle" and "twinkle" in  line:
        print(line)