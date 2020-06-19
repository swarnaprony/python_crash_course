#exercise_9_(4,5)
#date: 04/05/2020

#exercise_9_4
#number_served

class Restaurant:
    """A simple atempt to represent restaurant"""

    def __init__(self, name, cuisine_type):
        """initial attributes to describe a restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        print(f"the name of the restaurant is {self.name}")

    def describe_restaurant(self):
        """Description of restaurant"""
        print(f"The name of the restaurant is {self.name}")
        print(f"it's cuisine type is {self.cuisine_type} ")

    def open_restaurant(self):
        print(f"{self.name} is open now")

    def total_customer_served(self):
        """Show the number of customer served in this restaurant"""
        print(f"Number of customer served on this restaurant is {self.number_served}")

    def set_number_served(self,new_number):
        """Set the given value in Number_served"""
        self.number_served = new_number

    def increment_number_served(self,increment):
        """Increased the previous number_served with a given value"""
        self.number_served += increment

my_restaurant = Restaurant('aswan', 'Bangladeshi')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.total_customer_served()
my_restaurant.number_served = 15
my_restaurant.total_customer_served()
my_restaurant.set_number_served(17)
my_restaurant.total_customer_served()
my_restaurant.set_number_served(25)
my_restaurant.total_customer_served()
my_restaurant.increment_number_served(75)
my_restaurant.total_customer_served()

new_restaurant = Restaurant('Dominos Pizza', 'Italian')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
new_restaurant.number_served = 10
new_restaurant.total_customer_served()
new_restaurant.increment_number_served(12)
new_restaurant.total_customer_served()


#exercise_9_5
#login_attempts

class Users:
    """Initial attibutes to describe an user profile"""

    def __init__(self, first_name, last_name, age):
        """Initialize attributes to define User"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempt = 0

    def age_period(self):
        """Catagorige users in terms of age"""
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
        """Show users full name"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"name of the user is: {full_name}")
        print(f" Age of {full_name} is {self.age}")

    def login_attempts(self):
        """Show the number of login attempts"""
        print(f"the number of login attempts is {self.login_attempt}")

    def increment_login_attempts(self):
        """increased the value of login attempt by 1"""
        self.login_attempt +=1

    def reset_login_attempts(self):
        """Reset the previous login attempt value"""
        self.login_attempt = 0


user_1 = Users('mir', 'asif', 30)
user_1.describe_user()
user_1.age_period()

user_1.login_attempts()
user_1.increment_login_attempts()
user_1.login_attempts()

user_1.increment_login_attempts()
user_1.login_attempts()

user_1.reset_login_attempts()
user_1.login_attempts()


user_2 = Users('Swarna', 'Sarker', 293)
user_2.describe_user()
user_2.age_period()

user_3 = Users('Liza', 'Sarker', 32)
user_3.increment_login_attempts()
user_3.increment_login_attempts()
user_3.increment_login_attempts()
user_3.increment_login_attempts()
user_3.increment_login_attempts()
user_3.login_attempts()

user_3.reset_login_attempts()
user_3.login_attempts()
