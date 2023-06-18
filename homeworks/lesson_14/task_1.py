# Create a class Product with properties name, price, and quantity. 
# Create a child class Book that inherits from Product and adds a property author and a method called read.

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        pass

class Book(Product):
    def __init__(self, name: str, price: float, quantity: int, author: str, read: str):
        super().__init__(name, price, quantity)    
        