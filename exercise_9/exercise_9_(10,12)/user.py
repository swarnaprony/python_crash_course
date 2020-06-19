#exercise_9_11
#imported_admin
#main_class
#date: 17/06/2020

"""A simple attempt to define user class"""


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