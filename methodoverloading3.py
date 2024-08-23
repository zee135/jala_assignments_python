# 3. Methods with the Same Name and Same Number of Parameters of the Same Type

class MyClass:
    def show(self, value):
        print(f"Value: {value}")

    def show(self, value):
        print(f"Updated Value: {value}")

# Create an instance of MyClass
obj = MyClass()

# Call the show method
obj.show("Hello")  # Will call the last defined show method