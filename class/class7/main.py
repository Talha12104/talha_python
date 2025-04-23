# Traditional OOP Part
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

my_dog = Dog()
my_dog.speak()



class Car():
    def __init__(self, color, speed):
        self.color = color
        self.__speed = speed
        self.__engine = "V8"
        self.__wheels = 4
        self.__doors = 4
    def accelerate(self):
        self.__speed += 10
    def get_speed(self):
        return self.__speed

my_car = Car("red", 100)
print(my_car.color)