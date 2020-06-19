#function_practice
#date: 23/03/2020

from pizza import make_pizza as make_new_pizza, build_profile as build_new_profile

make_new_pizza(18, 'peeper', 'cheese')

user_profile = build_new_profile('swarna', 'sarker')
user_profile_1 = build_new_profile('swarna', 'sarker', profession = 'student', age = '29')
print(user_profile)
print(user_profile_1)

def build_profile(first, last, **user_info):
    print("this is our user profile: ")
    #print(f"first_name: {first}, last_name: {last}, {user_info}")
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('mir','asif', profession = 'engineer', age = '30')
print(user_profile)

def make_pizza(size, *toppings):
    print(f"make a pizza of size {size} ")
    for topping in toppings:
        print(f" add {topping}")

make_pizza(28,'olive')
make_pizza(32, 'olive','peeper','mashroom')


def elder_person_comparison(swan_family, asif_family):
    eldest_swan = eldest_person(swan_family,'swan')
    eldest_asif = eldest_person(asif_family, 'asif')
    if eldest_swan > eldest_asif :
        print(f"the older person is from swan_family and his age is {eldest_swan} ")
    else:
        print(f"the older person is from asif_family and his age is {eldest_asif} ")
def eldest_person(family, family_name):
    family = sorted(family)
    eldest_person = family[-1]
    print(f"the elder person in {family_name} family is of age {eldest_person}")
    return eldest_person

swan_family = [65, 29, 53, 37]
asif_family = [30, 70, 54]
elder_person_comparison(swan_family,asif_family)

def greet_users(names):
    for name in names:
        greet = f" Hello, {name.title()}"
        print(greet)
users = ['asif', 'liza']
greet_users(users)


def print_models(unprinted_designs, completed_model):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f" the current printed design is {current_design}")
        completed_model.append(current_design)
def show_completed_model(completed_model):
    for model in completed_model:
        print(f"the completed model is {model}")
unprinted_designs = ['kitchen','belcony','bedroom']
completed_model = []
print_models(unprinted_designs[:],completed_model)
show_completed_model(completed_model)
print(f" unprinted design {unprinted_designs}")
print(f" completed model {completed_model}")


def dic_full_name(first_name, middle_name = '', last_name = ''):
    if middle_name:
        if last_name:
            full_name = {'f_name': f"{first_name}", 'm_name': f"{middle_name}", 'l_name': f"{last_name}"}
        else:
            full_name = {'f_name': f"{first_name}", 'm_name': f"{middle_name}"}
    else:
        if last_name:
            full_name = {'f_name': f"{first_name}", 'l_name': f"{last_name}"}
        else:
            full_name = {'f_name': f"{first_name}"}
    return full_name
get_formated_full_name = dic_full_name('mir','asif')
print(get_formated_full_name)
#print(f"{get_formated_full_name['f_name']} {get_formated_full_name['m_name']} {get_formated_full_name['l_name']}")

def user_greetings():
    """Display a simple greetings"""
    #hello = input('write a greeting to your friend')
    print("hello asif")
user_greetings()

def greetings(username):
    """display username with greetings"""
    print(f"hello {username.title()}")
greetings('astu')


def greetings(username):
    """display username with greetings"""
    print(f"hello {username.title()}")
greetings('astu')
greetings('lu')

def describe_pet(animal_type, pet_name):
    print(f" the name of my {animal_type} is {pet_name.title()}")
describe_pet('dog', 'bolt')
describe_pet('cat', 'gerfield')
describe_pet('hamster', 'albin')
describe_pet('chicken', 'nigahiga')
describe_pet(animal_type = 'chicken', pet_name = 'nigahiga')

def describe_pet_1(pet_name, animal_type = 'dog'):
    print(f" the name of my {animal_type} is {pet_name.title()}")
describe_pet_1(pet_name = 'dooo')
describe_pet_1('doop')
describe_pet_1(animal_type = 'chicken', pet_name = 'nigahiga')

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
full_name = get_formatted_name('mir','asif')
print(full_name)

def max(x,y,z):
    if x>y:
        if x>z:
            return x
        else:
            return z
    else:
        if y>z:
            return y
        else:
            return z
max = max(-4,1,-7)
print(max)

def get_formated_full_name(first_name, last_name = '', middle_name = ''):
    if middle_name:
        if last_name:
            full_name = f"{first_name} {middle_name} {last_name}"
        else:
            full_name = f"{first_name} {middle_name}"
    else:
        if last_name:
            full_name = f"{first_name} {last_name}"
        else:
            full_name = f"{first_name}"
    return full_name.title()

show_full_name = get_formated_full_name('mir', 'asif', 'hossain')
print(show_full_name)
show_full_name = get_formated_full_name('swarna','sarker')
print(show_full_name)
show_full_name = get_formated_full_name('liza')
print(show_full_name)

def formated_inputed_name(first_name, middle_name = '',last_name = ''):
    if middle_name:
        if last_name:
            full_name = f"{first_name} {middle_name} {last_name}"
        else:
            full_name = f"{first_name} {middle_name}"
    else:
        if last_name:
            full_name = f"{first_name} {last_name}"
        else:
            full_name = f"{first_name}"
    return full_name.title()
while True:

    print('please input your first name: ')
    f_name = input("first_name: ")
    print('if you have a middle name input your middle name: ')
    m_name = input("middle_name: ")
    print('if you have a last name input your last name: ')
    l_name = input("last_name: ")

    formated_name = formated_inputed_name(f_name,m_name,l_name)
    print(formated_name)

    print("if you want to quit input 'quit' otherwise 'no': ")
    quit_program = input("'quit'/'no'")
    if quit_program == 'quit':
        break
while True:
    print("please tell me your name")
    print("enter 'quit' at any time you want to quit")
    f_name = input("first name: ")
    if f_name == 'quit':
        break
    m_name = input("middle name: ")
    if m_name == 'quit':
        break
    l_name = input("last name: ")
    if l_name == 'quit':
        break
    formated_name = formated_inputed_name(f_name,m_name,l_name)
    print(formated_name)



