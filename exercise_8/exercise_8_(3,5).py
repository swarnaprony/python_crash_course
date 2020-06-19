#exercise_8_(3,5)
#date: 23/03/2020

#exercise_8_3
#t-shirt

def make_tshirt(size, message):
    print(f"t-shirt size is {size}")
    print(message)
make_tshirt(size = '32', message = 'go for win')

#exercise_8_4
#large_tshirt

def make_tshirt(size = 'large', message = 'i love python'):
    print(f"t-shirt size is {size.title()}")
    print(message.title())
make_tshirt()
make_tshirt(size = 'large')
make_tshirt(size = 'medium')
make_tshirt(message = 'I LOVE JAVA')

#exercise_8_5
#cities

def describe_city(city, country_name = 'Germany'):
    print(f"{city.title()} is in {country_name.title()}")
describe_city('hamburg')
describe_city('elmshorn')
describe_city('dhaka')
