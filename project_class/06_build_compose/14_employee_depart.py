class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee, department_name):
        self.department_name = department_name
        self.employee = employee


emp = Employee("Asharib")
dept = Department(emp , "Teacher Faculty")
print(f"{dept.employee.name} works in {dept.department_name} department.")