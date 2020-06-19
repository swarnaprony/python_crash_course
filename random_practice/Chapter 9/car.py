#class_car
#date: 12/06/2020

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