class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn         # Private


emp = Employee("John", 50000, "123-45-6789")
print(emp.name)        # Works: John
print(emp._salary)     # Works but discouraged: 50000
try:
    print(emp.__ssn)   # Raises AttributeError
except AttributeError:
    print("Cannot access private variable __ssn")