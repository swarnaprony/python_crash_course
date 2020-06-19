#importing_a_function
#date: 07/04/2020


def make_pizza(size, *toppings):
    print(f"the size of the pizza is {size}")
    print(f"add topping: ")
    for topping in toppings:
        print(topping)


def build_profile(first, last, **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info
