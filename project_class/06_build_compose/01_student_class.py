class Student():
    def __init__(self, name:str, marks:int):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

student = Student("John Doe", 85)
student.display()