class Employee:
    company = "Microsoft"
    def show(self):
        print(f"This is your Name {self.company}.")

# class Programmer:
#     company = "Google"
#     def show(self):
#         print(f"This is your Name {self.name}.\nThis is your salary {self.salary}")

# class show_language:
#     def show(self):
#         print(f"This is your Name {self.name}.\nThis is your salary {self.salary}")

class Coder:
    language = "Python"
    def showlan(self):
        print(f"Out of all languages this is your {self.language}")

class Programmer(Employee, Coder):
    company = "Google"
    def show_language(self):
        print(f"This is name {self.company}\n and he good in {self.language}")

a = Employee()
b = Programmer()

b.show()
b.show_language()
b.showlan()