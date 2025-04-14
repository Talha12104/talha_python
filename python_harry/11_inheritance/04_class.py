class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class of value if {cls.a}")   

e = Employee()
e.a = 45
e.show()