# def sum(a:int,b:int):
#     return a+b
#     result = sum(10,20)
#     print(result)
#     return sum




# def sum(a:int) -> int:
#     a = 10
#     print(id(a))
#     return a
# num = 5
# result = sum(num)
# print(result)
# print(id(result))
# print(id(num))


# def main(a:list) -> list:
#     a.append(4)
#     print(f"A = {id(a)}")
#     return a 

# nums = [1,2,3]
# result = main(nums)
# print(id(result))
# print(id(nums))
# print(nums)

# Docstring is use to describe function description without finding the code by hover
# def greeting(name):
#     """This is the docstring greeting function"""
#     print("Hello {}.".format(name))
#     return

# greeting("Talha")
# greeting("Shayan")



# def printinfo(name, age):
#     "This print a passed info "



# def add(x:int,y:int = 0)-> float:
#     return float(x + y)

# print(float(add(10,20)))
# print(float(add(10.2,2.0)))
# print(float(add(10)))



# Unpack iterables Unlimited arguments

# def my_sum(*num):
#     print(type(num),".",num)
#     return sum(num)

# print(my_sum(1,2,3,4,5,))
# print(my_sum(*[1,2,3,4,5]))
# print(1,2,"Talha","Abc")


# Positional Only Argument

# def fun(x,y,/,z):
#     print(x + y + z)
#     return x, y, z
# print("Evaluating Positional Only Argument")
# print(1,4,z=4)


#Keyword Only Argument

# def fun(num,*,num1,num2,num3):
#     print(num * num1 * num2 * num3)


# Generator Function

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
    
# gen = simple_generator()
# print(next(gen))
# print(type(gen))

# for value in gen:
#     print(value,type(gen))


# def infinite_s():
#     num = 0
#     while True:
#         num += 1
#         if num == 100:
#             break
#         print(num)
# print(infinite_s())
    



# Recursive Function
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))


# Fibonacci Sequence
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif 