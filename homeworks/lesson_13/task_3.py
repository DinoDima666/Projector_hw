#  Create a Car class with the following attributes: brand, model, year, and speed. 
# The Car class should have the following methods: accelerate, brake and display_speed. 
# The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5. 
# Remember that the speed cannot be negative.

class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = max(0,speed)

    def accelerate(self):
        return self.speed + 5
    
    def brake(self):
        if self.speed - 5 < 0:
            return 0
        return self.speed - 5
        
    def display_speed(self):
        return self.speed
    

ford = Car("ford", "gt500 shelby", 1967, -5)    

print(ford.display_speed())
