#exercise_4_(3_9)
#date: 05/03/2020
#list_loop_range

#exercise_4_3
#counting_to_twenty

print([value for value in range(1,21)])

counting=[]
for value in range(1,21):
	counting.append(value)
print(counting)

#exercise_4_4
#list_of_one_million
one_million=list(range(1,101))
print(one_million)

million=[]
for value in one_million:
	million.append(value)
print(million)

print([value for value in range(1,101)])

#exercise_4_5
#summation_of_list
print(max(million))
print(min(million))
print(sum(million))

#exercise_4_6
#list_of_odd_numbers

odd_numbers=list(range(1,21,2))
print(odd_numbers)

odd_numbers_list=[]
for value in odd_numbers:
	odd_numbers_list.append(value)
print(odd_numbers_list)

print([value for value in range(1,21,2)])


#exercise_4_7
#list_of_multiple_of_3

multiple_three=list(range(3,31,3))
multiple_of_three=[]
for value in multiple_three:
	multiple_of_three.append(value)
print(multiple_of_three)

multiples_of_three=[]
for value in range(3,31,3):
	multiples_of_three.append(value)
print(multiples_of_three)

print([value*3 for value in range(1,11)])



#exercise_4_8
#list_of_qube

qube_list=[]
for value in range(1,11):
	values=value**3
	qube_list.append(values)
print(qube_list)

qubes_list=list(value**3 for value in range(1,11))
print(f"qube list {qubes_list}")
print([value**3 for value in range(1,11)])


#exercise_4_9
#list_of_qube_using_comprehension

print(f" comprehension {[value**3 for value in range(1,11)]}")




