class ClassOne:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from ClassOne, {self.name}!"

class ClassTwo:
    def __init__(self, age):
        self.age = age

    def age_info(self):
        return f"Age in ClassTwo is {self.age} years."

from .class_one import ClassOne
from .class_two import ClassTwo

from my_package import ClassOne, ClassTwo

def main():
    obj1 = ClassOne("Alice")
    obj2 = ClassTwo(30)

    print(obj1.greet())
    print(obj2.age_info())

if __name__ == "__main__":
    main()
