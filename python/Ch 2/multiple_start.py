# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

# MEGHA: Class C lists both classes A and B as its base classes 
class C(B,A):
    def __init__(self):
        super().__init__()

    def showProps(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()

c.showProps()

# MEGHA: Print method resolution order of Class C
# Output: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(C.__mro__)