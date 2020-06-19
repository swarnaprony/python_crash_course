#class_practice
#date: 08/04/2020

class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self, furniture):
        """Simulate a dog sitting in response to a command"""
        self.location = furniture
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate roll over in response to a command"""
        print(f"{self.name} rolled over")

    def get_location(self):
        print(f"{self.name} is sitting on {self.location}")

my_dog = Dog('puppy',1)
asif_dog = Dog('montu',2)

print(f"the name of my dog is {my_dog.name}")
print(f"the age of {my_dog.name} is {my_dog.age}")

my_dog.sit('chair')
my_dog.roll_over()
{my_dog.get_location()}
asif_dog.roll_over()


class Car:
    """A simple attemp to represent a car"""
    def __init__(self, maker, model, year):
        """initialize attributes to describe a car"""
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        full_name = f"{self.year} {self.maker} {self.model}"
        return full_name

    def read_odometer(self):
        """Print a statement showing car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You cannot roll back an odometer")

    def increment_odometer(self,miles):
        """ Add the given amount to the odometer Reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Print a simple mesaage to fill the tank"""
        print("You have to fill the gas tank as soon as possible")

car_1 = Car('BMW', 'B2', 2002)
print(car_1.get_descriptive_name())
car_1.read_odometer()

car_1.odometer_reading = 20
car_1.read_odometer()

car_1.update_odometer(15)
car_1.read_odometer()

car_1.increment_odometer(50)
car_1.read_odometer()


class Battery:
    """A simple attempt to model a battery for an electric class"""

    def __init__(self, battery_size = 75):
        """Initializing a battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describes the battery size"""
        print(f"This car has a {self.battery_size}-KWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        if self.battery_size == 100:
            range = 315

        print(f"The car can go about {range} miles on a full charge")



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, maker, model, year):
        """Initiatize attibutes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(maker, model , year)
        self.battery = Battery()

    
    def fill_gas_tank(self):
        """Electric car don't have gas tank"""
        print(f"This car does not need a gas tank")



my_tesla = ElectricCar('Tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.update_odometer(50)
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
