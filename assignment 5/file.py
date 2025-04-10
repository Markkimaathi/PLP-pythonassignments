#  Design  Class

class Superhero:
    def __init__(self, name, age, superpower, city, weakness):
        self.name = name
        self.age = age
        self.superpower = superpower
        self.city = city
        self.__weakness = weakness  # Encapsulated attribute

    def introduce_self(self):
        print(f"Hello, I'm {self.name}, protector of {self.city}! I'm {self.age} years old and my superpower is {self.superpower}.")

    def use_power(self):
        print(f"{self.name} is using {self.superpower} to save the day!")

    def reveal_weakness(self):
        print(f"Shh... my weakness is {self.__weakness}.")

    def get_weakness(self):
        return self.__weakness

class Villain(Superhero):
    def introduce_self(self):
        print(f"Ah, I am {self.name}, the terror of {self.city}! My power is {self.superpower} and I am {self.age} years old.")

    def commit_crime(self):
        print(f"{self.name} is committing a crime using {self.superpower}!")

#  Polymorphism Challenge

class Vehicle:
    def move(self):
        print("This vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying...")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing...")

# Example Usage

# Superhero and Villain
hero = Superhero("Flash", 25, "Super Speed", "Central City", "Cold")
villain = Villain("Reverse-Flash", 30, "Negative Speed Force", "Central City", "Heat")

hero.introduce_self()
hero.use_power()
print(f"Hero's weakness: {hero.get_weakness()}")
print()

villain.introduce_self()
villain.commit_crime()
print()

# Vehicles
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()