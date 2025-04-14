class Employee:
    language = "Python"
    salary = 120000

    def __init__(self, name, age, salary, language):
        self.name = name
        self.age = age
        self.language = language
        self.salary = salary
        print(f"Employee Info\n")

    def get_info(self):
        print(f'Your Known Language {self.language}.\nYour salary is {self.salary}')

    @staticmethod
    def greet():
        print("Good Morning")

talha = Employee("Talha",19,"Python",120000)
print(talha.name, talha.age, talha.salary, talha.language)
