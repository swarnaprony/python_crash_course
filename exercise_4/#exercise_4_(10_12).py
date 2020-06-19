#exercise_4_(10_12)
#date: 05/03/2020
#slicing_list


#exercise_4_10
#use_of_slices

numbers_list=list(value**3 for value in range(1,11))
print(numbers_list)

print(numbers_list[:3])
print(f"Three of the item from middle are: {numbers_list[4:7]}")
print(f"Last three item from the list: {numbers_list[-3:]}")


#exercise_4_11
#copying_list

favourite_pizzas=["supreme","papparoni","hawai","chicken","mashroom"]
friend_pizzas=favourite_pizzas[:]
favourite_pizzas.append("dhakai")
friend_pizzas.append("london")
print(f"my favourite pizzas are: {[values for values in favourite_pizzas]}")
print(f"my friends favourite pizzas are: {[value for value in friend_pizzas]}")

#exercise_4_12
#use_of_for_loop

for value in favourite_pizzas:
	print(value) 

for value in friend_pizzas:
	print(f"\n {value}")