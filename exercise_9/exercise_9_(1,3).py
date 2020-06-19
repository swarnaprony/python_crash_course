#exercise_9_(1,3)
#date: 09/04/2020

#exercise_9_1
#restaurants

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

#exercise_9_2
#three_restaurants

restaurant_1 = Restaurant('Macdonalds', 'American')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('Rajasthani', 'Indian')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Mr. Kebap', 'Turkish')
restaurant_3.describe_restaurant()

#exercise_9_3
#users

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
