#exercise_6_(1,3)
#date: 13/03/2020
#dictionary_exercise

#exercise_6_1
#person

persons_list = {
    'asif': {'first_name': 'mir', 'last_name': 'hossain', 'age': '30', 'city': 'elmshorn'},
    'lu': {'first_name': 'liza', 'last_name': 'sarker', 'age': '32', 'city': 'upsala'},
    'ri': {'first_name': 'ripa', 'last_name': 'sarker', 'age': '33', 'city': 'mymensingh'},
    'di': {'first_name': 'supta', 'last_name': 'sarker', 'age': '37', 'city': 'dhaka'},
    }
print(persons_list)

#exercise_6_2
#favourite_numbers

favourite_numbers = {
    'astu': '7',
    'swan': '13',
    'ri': '1',
    'di': '100',
    'lu': '1',
    }
for key in favourite_numbers:
    print(f"{key} : {favourite_numbers[key]}")
print(favourite_numbers)

#exercise_6_3
#glossary

glossary = {
    'list': 'store values',
    'for': 'looping',
    'if': 'conditioning',
    'del': 'delete values',
    'sort': 'sort and change',
    }
for key in glossary:
    print(f"{key} : {glossary[key]}")
print(glossary)

for key in glossary:
    print(f"{key} : \n{glossary[key]}")
print(f"{glossary.get('si','not in the list')}")

asif_0 = {
    'first_name': 'mir',
    'last_name': 'hossain',
    'age': '30',
    'city': 'elmshorn',
    }    

for key, value in asif_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

favourite_numbers_0 = {
    'astu': '7',
    'swan': '13',
    'ri': '1',
    'di': '100',
    'lu': '1',
    }
for name,number in favourite_numbers_0.items():
    print(f"{name}'s favourite number is: {number}")

for name in favourite_numbers_0.keys():
    print(f"{name}'s has favourite number")

for name in favourite_numbers_0:
    print(f"{name.title()}'s has favourite number")
sisters=['lu','ri','di']
for name, number in favourite_numbers.items():
    print(f"Hi just {name}")
    if name in sisters:
        print(f"sister {name} your favourite number is: {number} ")
if 'maa' not in favourite_numbers_0.keys():
    print(f'maa is not in the list')
for name in sorted(favourite_numbers_0.keys()):
    print(f"{name.title()}, you are in the list")
for number in favourite_numbers_0.values():
    print(number)
for number in set(favourite_numbers_0.values()):
    print(number)
names={'lu','ri','ri'}
print(names)