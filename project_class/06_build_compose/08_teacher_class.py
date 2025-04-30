class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


teacher = Teacher("Asharib", "Html")
print(f"{teacher.name} teaches {teacher.subject}")  # Output: Alice teaches Math