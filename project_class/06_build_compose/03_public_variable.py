class Car():
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start(self):
        print(f"{self.color} {self.brand} is starting.")

car = Car("red", "Toyota")
car.start()