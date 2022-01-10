# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages 
        self.price = price 
        self.__secret = "this is a secret attribute"

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount/100)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

# TODO: create instances of the class
b1 = Book("Brave New World","LT", 125, 45)
b2 = Book("War and Peace", "JDS", 12, 45)


# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
b1.setdiscount(25)
print("Price of book1: ", b1.getprice())
print("Price of book2: ", b2.getprice())


# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)