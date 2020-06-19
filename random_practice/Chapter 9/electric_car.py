#electric_car.py module

"""A set of classes that can be used to represent a electric car."""


from car import Car

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
