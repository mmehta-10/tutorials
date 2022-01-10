# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title):
        self.title = title


# TODO: create instances of the class
b1 = Book("Brave New World")
b2 = Book("War and Peace")

# TODO: print the class and property
print(b1)
print(b2.title)
