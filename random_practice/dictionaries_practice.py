#dictionaries_practice
#date: 12/03/2020

alien_0 = {'colour': 'green', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"you have earned {new_points} points")
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

alien_1 = {'birth_place': {'planet_name': {'country_name': 'bangladesh'}}}
print(alien_1['birth_place'])

alien_2 = {}
alien_2['colour'] = 'blue'
alien_2['points'] = 10
print(alien_2)
alien_2['colour'] = 'yellow'
print(alien_2)

alien_3={'x_position': 0, 'y_position': 25, 'speed': "medium"}
if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_3['x_position'] = alien_3['x_position'] + x_increment
alien_3['speed'] = "fast"
print(alien_3['x_position'])
print(alien_3)

del alien_3['speed']
print(alien_3)

favourite_language = {
    'asif': 'java',
    'swan': 'python',
    'supta': 'r',
    'ri': 'r',
    }
language = favourite_language['asif'].title()
print(favourite_language)
print(f"asif's favourite language is {favourite_language['asif'].title()}")
print(f"asif's favourite language is {language}")
liza_favourite = favourite_language.get('liza','no liza is assinged')
ri_favourite = favourite_language.get('ri','ri is not assinged')
print(liza_favourite)
print(ri_favourite)
ripa_favourite = favourite_language.get('ripa')
print(ripa_favourite)

#nesting

alien_0 = {'colour': 'blue', 'point': '10'}
alien_1 = {'colour': 'red', 'point': '15'}
alien_2 = {'colour': 'black', 'point': '20'}
alien = [alien_0,alien_1,alien_2]
for aliens in alien:
    print(aliens)

aliens = []
for alien_number in range(30):
    new_alien = {'colour': 'red', 'point': '5', 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print(len(aliens))

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'fast'
        alien['point'] = '10'
    elif alien['colour'] == 'red':
        alien['colour'] = 'purple'
        alien['speed'] = 'medium'
        alien['point'] = '15'
for alien in aliens[:5]:
    print(alien)
pizza = {
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'],
    }
print(f"you ordered a pizza with {pizza['crust']} crust and following toppings:")
for toppings in pizza['toppings']:
    print(f"{toppings}")
favourite_languages = {
    'asif': ['java','cotlin','python'],
    'ri': [],
    'lu': ['r','python'],
    'di': ['r','c++'],
    'swan': ['fortran','python'],
}
for keys,values in favourite_languages.items():
    print(f"{keys} love programing language:")
    for value in values:
        print(value)

favourite_languages = {
    'asif': ['java','cotlin','python'],
    'ri': [],
    'lu': ['r'],
    'di': ['r','c++'],
    'swan': ['fortran','python'],
}
for key,languages in favourite_languages.items():
    if len(languages) >= 2:
        print(f"{key}'s favourite languages are:")
        for language in languages:
            print(language)
    elif 1 <= len(languages) < 2:
        print(f"{key}'s favourite language is:")
        for language in languages:
            print(language)
    else:
        print(f"{key}'s has no favourite language")

users = {
    'asif': {
        'first_name': 'mir',
        'last_name': 'hossain',
        'location': 'elmshorn',
    },
    'lu': {
        'first_name': 'liza',
        'last_name': 'sarker',
        'location': 'upsala',
    }
}
for user_name,user_info in users.items():
    print(f"user name: {user_name} full name: {user_info['first_name']} {user_info['last_name']}")
    print(f"location is {user_info['location'].title()}")