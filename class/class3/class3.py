my_string : str = "Muhammad Talha"
my_string1 : str = ""
print(len(my_string))
print(my_string[0:3])

print([method for method in dir(str) if "__" not in method])
print(my_string.capitalize())
print(my_string.casefold())
print(my_string.upper())
print(my_string.lower())
print(my_string.split())
print(my_string1.join(["Muhammad ","Talha"]))
print(my_string.replace("Talha", "Shayan"))
print(my_string.find("Talha"))

starting_index = my_string.find("Muhammad")
my_string = starting_index + len("Muhammad")
count = my_string.count("Talha")
print(count)