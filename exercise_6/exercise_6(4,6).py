#exercise_6(4,6)
#date: 14/03/2020

#exercise_6_4
#glossary_2
favourite_colours = {
    'lu': 'blue',
    'ri': 'pink',
    'di': 'purple',
    'mona':'red',
    }
for keys,values in favourite_colours.items():
    print(f"name: {keys} favourite colour: {values}")

glossary_2 = {
    'list': 'store values',
    'for': 'looping',
    'if': 'conditioning',
    'del': 'delete values',
    'sort': 'sort and change',
    'item': 'for iterating keys and values from dictionaries',
    'keys': 'for iterating only keys from dictionaries',
    'values': 'for iterating only values from dictionaries',
    }
for keys,values in glossary_2.items():
    print(f"{keys} means {values}")

#exercise_6_5
#rivers

rivers = {
   'elbe':  'germany',
   'padma': 'bangladesh',
   'ganga': 'india',
   'jamuna': 'india',
   'jamuna': 'bangladesh',
   }
for keys,values in rivers.items():
    print(f"{keys} runs through {values} ")
for keys in rivers.keys():
    print(f"{keys} is a river")
for values in rivers.values():
    print(f"{values} have rivers")

#exercise_6_6
#working_with_pool

favourite_language_1 = {
    'asif': 'java',
    'swan': 'python',
    'supta': 'r',
    'ri': 'r',
    'zeejun': 'c'
    }
take_poll = ['mummum','mummin','maa','zeeja','ri','lu','asif']
for name in take_poll:
    if name in favourite_language_1.keys():
        print(f"thank you {name} for taking the poll")
    else:
        print(f"{name} please take the poll")