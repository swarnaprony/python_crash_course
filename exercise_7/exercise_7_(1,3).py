#exercise_7_(1,3)
#date: 17/03/2020

#exercise_7_1
#rental_car

rental_car = input('what kind of car do you want? ')
print(f"\n let me see if {rental_car} is available.")

#exercise_7_2
#restaurant_seating

persons = input('how many persons are in your dinner group? ')
if int(persons) > 8:
    print(f"seat for {persons} is not available now. have to wait")
else:
    print('your table is ready')

#exercise_7_3
#multiples_of_ten

multiple = input('give a number multiple of 10')
if int(multiple) % 10 == 0:
    print(f"{multiple} is a multiple of 10")
else:
    print(f"{multiple} is not a multiple of 10")