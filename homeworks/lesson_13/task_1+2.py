class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other_country):
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        return   Country(combined_name, combined_population) 


# class Country:
#     def __init__(self, name: str, population: int):
#         self.name = name
#         self.population = population
#     def __add__(self, other):
#         if type(other) != Country:
#             return TypeError("Other must be a Country instance")    
#         combined_name = f"{self.name} {other.name}"
#         combined_population = self.population + other.population
#         return Country(combined_name, combined_population)



bosnia = Country('Bosnia', 10_000_000)

herzegovina = Country('Herzegovina', 5_000_000) 

bosnia_herzegovina = bosnia.add(herzegovina)

# bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina.name)
print(bosnia_herzegovina.population)

