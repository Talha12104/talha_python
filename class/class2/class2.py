# Store String Variable
text : str = "Hello World"
# Store integer Value of Number
numbers : int = 2
# Store Decimal Value of Number
decimal_value : float = 5.5
# Boolean Variable for True And False
boolean : bool = True
# list which store data like array and it's able to change
coll_of_data : list[int] = [1,2,3,4,5,6,7,8]
# tuple is immutable does'nt change when created
immutable_data : tuple[int,str,int,int,float] = (1,"Talha",3,14,0.5)
# Dict for call data by keyvalue and its use for object 
object_data : dict[str,str] = {"name":"Talha","age":"20","father_name":"Muhammad Ramzan"}
# set for unique data which does'nt repeat and change and sometime ordered
unique_values : set[int] = {1,4,6,2,3,5,1}
# frozenset for immutable set it doesn't change
unique_values : frozenset[int] = {1,4,6,2,3,5,1}

# number_list : list[int] = range(1,20)
# numberlist for loop
for num in range(1,20):
    number_list : list[int] = []
    number_list.append(num)


# byte list
byte_list : bytearray =([2,3,5,6,7])
print(byte_list)

a = 6
b = a
b = 7
print(id(a),id(b))


# print(c)
# print(type(c))
# print(str(c))
# print(float(c))
# c = str(c)
# print(type(c)) 

# pylance insistance
c : int = 8
# if type(c) == int:
# print("c ia an integer")
# else:
#     print("c ia not integer")

print(isinstance(c,int))
print(isinstance(c,float))



# Logical Operators X and Y = Operands + and = is Operator and Z is Result
a = 2
b = 3
z = a ** b # + - % // **
print(f"A + B = {z}")

# Not logical Operators
# Bool True and False
if (2==3):
    print(False)
else:
    print(True)

print(a is b)

# Binary Operators
x : int = 5
y : int = ~x
print(y)

# Comparison Operators
# == | >= | <= | !- or not | < | >
# and =  True & False
# or = True or False or False = True

# Assigment Operators
# -= | += | /= | //= | *= | %=

# Membership Operators
# in | not in
l : list[int] = [1,2,3,4,5]
i = 6
print(i in l )
print(i not in l )
