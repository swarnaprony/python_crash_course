#exercise_9_10
#imported_restaurant
#main_class
#date: 16/06/2020

"""A simple attempt to store a Restaurant class"""

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
        print(f"{self.name} is open now")

my_restaurant = Restaurant('aswan', 'Bangladeshi')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

new_restaurant = Restaurant('Dominos Pizza', 'Italian')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
