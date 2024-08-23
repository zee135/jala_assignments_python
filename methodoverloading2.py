# 2. Methods with the Same Name but Different Number of Parameters of Different Data Types


class MyClass:
    def display(self, value):
        if isinstance(value, int):
            print(f"Integer value: {value}")
        elif isinstance(value, str):
            print(f"String value: {value}")
        else:
            print("Unsupported type")

    def display(self, value1, value2):
        print(f"First value: {value1}, Second value: {value2}")

# Create an instance of MyClass
obj = MyClass()

# Call the display method with different types and number of parameters
obj.display(10)             # Will call the last defined display method with two parameters
obj.display("Hello")       # Will also call the last defined display method with two parameters
obj.display(10, "World")   # Will call the display method with two parameters
