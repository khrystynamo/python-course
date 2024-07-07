#1. Create add method to add two countries together. 
# This method should create another country object 
# with the name of the two countries combined and 
# the population of the two countries added together.

class Country:
    def __init__(self, country_name, population):
        self.country_name = country_name
        self.population = population
    
    def add(self, other_country):
        new_name = f"{self.country_name} {other_country.country_name}"
        new_population = self.population + other_country.population
        return Country(new_name, new_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population) 
print(bosnia_herzegovina.country_name)

#2. Implement the previous method with a magic method

class Country:
    def __init__(self, country_name, population):
        self.country_name = country_name
        self.population = population
    
    def __add__(self, other_country):
        new_name = f"{self.country_name} {other_country.country_name}"
        new_population = self.population + other_country.population
        return Country(new_name, new_population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population) 
print(bosnia_herzegovina.country_name)

# 3. Create a Car class with the following attributes: brand, model, year, and speed. 
# The Car class should have the following methods: accelerate, brake and display_speed. 
# The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5. 
# Remember that the speed cannot be negative.

class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5
    
    def break_speed(self):
        if self.speed <= 5:
            print('Minimal speed')
        else: 
            self.speed -= 5
    
    def display_speed(self):
        print(f'The speed is {self.speed}')
    
    
mazda = Car('Mazda','3', '2018')
mazda.speed
mazda.accelerate()
mazda.display_speed()
mazda.break_speed()
mazda.display_speed()
mazda.break_speed()
mazda.display_speed()