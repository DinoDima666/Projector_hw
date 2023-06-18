# Create a class Restaurant with properties name, cuisine, and menu. 
# The menu property should be a dictionary with keys being the dish name and values being the price. 
# Create a child class FastFood that inherits from Restaurant 
# and adds a property drive_thru (a boolean indicating whether the restaurant has a drive-thru or not) 
# and a method called order which takes in the dish name and quantity and returns the total cost of the order. 
# The method should also update the menu dictionary to subtract the ordered quantity from the available quantity. 
# If the dish is not available or if the requested quantity is greater than the available quantity, 
# the method should return a message indicating that the order cannot be fulfilled. 

class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: dict, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru
    def order(self, dish, amount):
        if self.drive_thru == False:
            return "Drive through service is not available"    
        
        if dish not in self.menu:
            return "Dish is not available"
        
        elif self.menu[dish]["quantity"] < amount: 
            return "Requested quantity not available"
        
        else:
            self.menu[dish]["quantity"] -= amount
            return self.menu[dish]["price"] * amount



menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available


