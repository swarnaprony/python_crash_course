#exercise_8_module
#printing_function

def print_name(first, last, **user_info):
    """print the info of user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


def print_name_again():
    print("Good Morning")