class Company:
    companies = ["Google", "Microsoft", "Nvidia"]

class Employee(Company):
    def __init__(self, name, age, company, language):
        self.name = name
        self.age = age
        self.company = company
        self.language = language

    def get_salary(self):
        if self.language == "Python":
            return 150000
        elif self.language == "Javascript":
            return 90000
        elif self.language == "Typescript":
            return 100000
        else:
            return 0

def main():
    employees = []
    languages = ["Python", "Typescript", "Javascript"]

    while True:
        name = input("Enter Your Name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        age = int(input("Enter your Age: "))
        
        print("Choose your company:")
        for i, company in enumerate(Company.companies, 1):
            print(f"{i}. {company}")
        company_choice = int(input("Enter the number of your company: "))
        company = Company.companies[company_choice - 1]

        print("Choose your language:")
        for i, language in enumerate(languages, 1):
            print(f"{i}. {language}")
        language_choice = int(input("Enter the number of your language: "))
        language = languages[language_choice - 1]

        employee = Employee(name, age, company, language)
        salary = employee.get_salary()
        employee_info = {
            "name": employee.name,
            "age":  employee.age,
            "company": employee.company,
            "language":  employee.language,
            "salary": salary
        }
        employees.append(employee_info)
        print(f"Employee Info: {employee_info}")

    print("\nAll Employees:")
    for emp in employees:
        print(emp)

if __name__ == "__main__":
    main()