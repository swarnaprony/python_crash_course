#exercise_3_(8-11)
#date: 04/03/2020
#places_want_to_visit

#exercise_3_8
#list_of_location

desired_places=["swizweland","indonesia","bhutan","norway","india"]
print(desired_places)
print(sorted(desired_places))
print(desired_places)
desired_places.reverse()
print(desired_places)
desired_places.reverse()
print(desired_places)
desired_places.sort()
print(desired_places)
desired_places.sort(reverse=True)
print(desired_places)

#exercise_3_9
#length_of_list_of_3_3

invite_them=["lu","ri","di"]
print(f"number of people i invited to dinner is {len(invite_them)}")

#exercise_3_10
#use_of_every_function

favourite_foods=["biriani","mutton","chips","icecream","muri"]
print(f"Most favourite one is {favourite_foods[1]}")
favourite_foods[2]="shahputin"
print(favourite_foods)
favourite_foods.append("porota")
print(favourite_foods)
favourite_foods.insert(3,"frenchfries")
print(favourite_foods)
del favourite_foods[4]
print(favourite_foods)
popped_item=favourite_foods.pop(2)
print(f"want to eat {popped_item} again")
favourite_foods.remove("muri")
print(favourite_foods)
favourite_foods.reverse()
print(favourite_foods)
print(sorted(favourite_foods))
favourite_foods.sort()
print(favourite_foods)
favourite_foods.sort(reverse=True)
print(favourite_foods)
print(len(favourite_foods))

#exercise_3_11
#common_error_in_list

print(favourite_foods[-1])
