#exercise_6_(7,12)
#date: 16/03/2020

#exercise_6_7
#people

people_1 = {
'name': 'asif',
'age': '30',
'occupation': 'engineer',
}
people_2 = {
'name': 'lu',
'age': '32',
'occupation': 'chef',
}
people_3 = {
'name': 'ri',
'age': '34',
'occupation': 'mother',
}
people_4 = {
'name': 'di',
'age': '37',
'occupation': 'researcher',
}
people = [people_1, people_2, people_3,people_4]
for man in people:
    print(man)

#exercise_6_8
#pets

pet_1={'name': 'cat', 'owner_name': 'mummmin'}
pet_2={'name': 'dog', 'owner_name': 'mummum'}
pets=[pet_1,pet_2]
for pet in pets:
    print(pet)

#exercise_6_9
#favourite_places

favourite_places = {
    'asif': ['mongolia','norway','corsica','egypt'],
    'lu': ['newzeland','finland','sweden'],
    'ri': ['germany','india','sweden'],
}
for name,places in favourite_places.items():
    print(f"{name}'s favourite places are:")
    for place in places:
        print(place)

#exercise_6_10
#favourite_numbers

favourite_numbers = {
    'astu': ['7','3','13'],
    'swan': ['13','3'],
    'ri': ['1'],
    'di': ['1','100'],
    'lu': ['1'],
    }
for name,number in favourite_numbers.items():
    if len(number) >= 2:
        print(f"{name} favourite numbers are:")
        for value in number:
            print(value)
    else:
        print(f"{name} favourite number is:")
        for value in number:
            print(value)

#exercise_6_11
#cities

cities = {
    'hamburg': {
        'area': '1000',
        'population': '1million',
        'country': 'germany',
        },
    'dhaka': {
        'area': '900',
        'population': '100million',
        'country': 'bangladesh',
        },
    'dehli': {
        'area': '1050',
        'population': '2million',
        'country': 'india',
        },
}
for city,info in cities.items():
    print(f"\nname of the city {city}")
    for key,value in info.items():
        print(f"\n{key}: {value}")

#exercise_6_12
#extensions

for city,info in cities.items():
    new_info={'look': 'beautiful'}
    city['info'].append(new_info)
    if city=='hamburg':
            info['area'] = '1100'
    print(info)