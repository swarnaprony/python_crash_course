#exercise_9_(6,9)
#date: 11/06/2020

#exercise_9_6
#Ice_Cream_Stand

class Restaurant:
    """A simple atempt to represent restaurant"""

    def __init__(self, name, cuisine_type):
        """initial attributes to describe a restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type
        print(f"the name of the restaurant is {self.name}")

    def describe_restaurant(self):
        """Description of restaurant"""
        print(f"The name of the restaurant is {self.name}")
        print(f"it's cuisine type is {self.cuisine_type} ")

    def open_restaurant(self):
        """A simple attempt to print the current status of the restaurant"""
        print(f"{self.name} is open now")


class Ice_Cream_Stand(Restaurant):
    """A simple attempt to represent a specific kind of restaurant"""

    def __init__(self, name, cuisine_type):
        """Initializing attributes of parent class"""
        """ and then initializing attributes specific to this class"""
        super().__init__(name, cuisine_type)
        self.flavours = ['chocholate','strawberry']

    def flavours_available(self):
        """simple attempt to print the flavours available"""
        for flavour in self.flavours:
            print(f"Flavours available are {flavour}")

new_restaurant = Ice_Cream_Stand('Ice Cream Stand', 'Desert')
new_restaurant.flavours_available()
new_restaurant.describe_restaurant()


#exercise_9_7
#Admin_Class


class Users:
    """Initial attibutes to describe an user profile"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def age_period(self):
        if self.age <= 12:
            print(f"{self.first_name} is a child")
        elif 12 < self.age < 18:
            print(f"{self.first_name} is a teenager")
        elif 18 <= self.age < 30:
            print(f"{self.first_name} is young")
        elif 30 <= self.age < 60:
            print(f"{self.first_name} is an adult")
        else:
            print(f"{self.first_name} is a old person")
        
    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"name of the user is: {full_name}")
        print(f" Age of {full_name} is {self.age}")

user_1 = Users('mir', 'asif', 30)
user_1.describe_user()
user_1.age_period()

user_2 = Users('Swarna', 'Sarker', 293)
user_2.describe_user()
user_2.age_period()


#exercise_9_8
#privileges


class Privileges:
    """Represent a aspects of Users class, specific to admin"""

    def __init__(self, admins_privilege = ['Can add post', 'Can delete post', 'Can ban user']):
        """Initialize the attributes of the parent class
        then intialize the attributes specific to admin class"""
        self.admins_privilege = admins_privilege

    def show_privileges(self):
        """Print the privileges of an admin"""
        for privilege in self.admins_privilege:
            print(f" An admin {privilege}")


class Admin(Users):
    """Represent a aspects of Users class, specific to admin"""

    def __init__(self, first_name, last_name, age):
        """Initialize the attributes of the parent class
        then intialize the attributes specific to admin class"""
        super().__init__(first_name, last_name, age)
        self.new_privilege = Privileges()

new_user = Admin('Mir', 'Asif', 30)
new_user.new_privilege.show_privileges()


#exercise_9_9
#Battery_Upgrade

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


    def upgrade_battery(self):
        """A attempt to upgrade battery of electric car"""
        if self.battery_size <= 100:
            print(f"The capacity of this car's battery is {self.battery_size}")

        else:
            self.battery_size = 100
            print(f" The capacity of this car's battery is upgraded to 100")



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
my_tesla.battery.upgrade_battery()


