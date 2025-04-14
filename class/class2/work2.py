# Python Data Types
# 1. Numeric Types
integer_num = 10
float_num = 3.14
complex_num = 2 + 3j

# 2. String Type
text = "Hello World"
char = 'A'

# 3. Boolean Type
is_true = True
is_false = False

# 4. List Type (ordered, mutable)
my_list = [1, 2, 3, "apple", True]

# 5. Tuple Type (ordered, immutable)
my_tuple = (1, 2, 3, "apple")

# 6. Set Type (unordered, unique elements)
my_set = {1, 2, 3, 4}

# 7. Dictionary Type (key-value pairs)
my_dict = {"name": "John", "age": 30}

# 8. None Type
empty_value = None
print(f"None value: {empty_value}")

# Python Operators
# 1. Arithmetic Operators
a, b = 10, 3
addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333...
floor_division = a // b # 3
modulus = a % b        # 1
exponent = a ** b      # 1000

# 2. Comparison Operators
equal = a == b         # False
not_equal = a != b     # True
greater = a > b        # True
less = a < b          # False
greater_equal = a >= b # True
less_equal = a <= b   # False

# 3. Logical Operators
x, y = True, False
and_result = x and y   # False
or_result = x or y     # True
not_result = not x     # False

# 4. Assignment Operators
c = 5                  # Simple assignment
c += 3                 # c = c + 3
c -= 2                 # c = c - 2
c *= 2                 # c = c * 2
c /= 2                 # c = c / 2

# 5. Identity Operators
is_same = a is b       # False
is_not_same = a is not b # True

# 6. Membership Operators
in_list = 1 in my_list     # True
not_in_list = 10 not in my_list  # True

 

print("\n--- Operators Results ---")
print("Arithmetic Operators:")
print(f"Addition (a + b): {addition}")
print(f"Subtraction (a - b): {subtraction}")
print(f"Multiplication (a * b): {multiplication}")
print(f"Division (a / b): {division}")
print(f"Floor Division (a // b): {floor_division}")
print(f"Modulus (a % b): {modulus}")
print(f"Exponent (a ** b): {exponent}")

print("\nComparison Operators:")
print(f"Equal (a == b): {equal}")
print(f"Not Equal (a != b): {not_equal}")
print(f"Greater (a > b): {greater}")
print(f"Less (a < b): {less}")
print(f"Greater Equal (a >= b): {greater_equal}")
print(f"Less Equal (a <= b): {less_equal}")

print("\nLogical Operators:")
print(f"AND (x and y): {and_result}")
print(f"OR (x or y): {or_result}")
print(f"NOT (not x): {not_result}")

print("\nMembership and Identity Operators:")
print(f"Is Same (a is b): {is_same}")
print(f"Is Not Same (a is not b): {is_not_same}")
print(f"In List (1 in my_list): {in_list}")
print(f"Not In List (10 not in my_list): {not_in_list}")
# 7. Bitwise Operators
x = 10  # 1010 in binary
y = 4   # 0100 in binary

bitwise_and = x & y    # 0 (0000)
bitwise_or = x | y     # 14 (1110)
bitwise_xor = x ^ y    # 14 (1110)
bitwise_not = ~x       # -11 (inverts all bits)
left_shift = x << 2    # 40 (101000)
right_shift = x >> 2   # 2 (10)

print("\nBitwise Operators:")
print(f"Bitwise AND (x & y): {bitwise_and}")
print(f"Bitwise OR (x | y): {bitwise_or}")
print(f"Bitwise XOR (x ^ y): {bitwise_xor}")
print(f"Bitwise NOT (~x): {bitwise_not}")
print(f"Left Shift (x << 2): {left_shift}")
print(f"Right Shift (x >> 2): {right_shift}")