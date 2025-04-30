class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says Woof!")

    def show_breed(self):
        print(f"{self.name} is a {self.breed}.")


dog = Dog("Max", "Labrador")
dog.bark()
dog = Dog("Max", "Labrador")
dog.show_breed()