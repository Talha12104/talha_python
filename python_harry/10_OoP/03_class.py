class Employee:
    language = "Python"
    salary = 120000

    def get_info(self):
        print(f'Your Known Language {self.language}.\nYour salary is {self.salary}')

    @staticmethod
    def greet():
        print("Good Morning")

talha = Employee()
# talha.language = "TypeScript"
print(talha.language, talha.salary)
talha.greet()
talha.get_info