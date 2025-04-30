def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass

# Example usage
p = Person()
print(p.greet())  # Output: Hello from Decorator!