# 1. Methods with the Same Name but Different Number of Parameters of the Same Type

class MyClass:
    def greet(self, name):
        print(f"Hello, {name}!")

    def greet(self, name, greeting="Hello"):
        print(f"{greeting}, {name}!")

# Create an instance of MyClass
obj = MyClass()

# Call the greet method with different numbers of parameters
obj.greet("Alice")          # Uses the method with one parameter
obj.greet("Bob", "Hi")      # Uses the method with two parameters




