#exercise_8_(12,14)
#date: 07/04/2020

#exercise_8_12
#sandwiches

def sandwiches(*items):
    for item in items:
     print(f"add {item}")
sandwiches('peeper')
sandwiches('peeper','extra_cheese')
sandwiches('olive', 'chicken', 'onion', 'mashroom')

#exercise_8_13
#user_profile

def build_profile(first, last, **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info
user_profile = build_profile('swarna', 'sarker')
user_profile_1 = build_profile('swarna', 'sarker', profession = 'student', age = '29')
print(user_profile)
print(user_profile_1)

#exercise_8_14
#cars

def cars(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer.title()
    car_info['model_name'] = model.title()
    return car_info
car_profile = cars('toyota', 'premier', colour = 'black', mileage = '1800' )
print(car_profile)