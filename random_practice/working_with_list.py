#working_with_list_practice
#date:04/03/2020


my_friends=["astu","lu","ri","mummum","shampu","nit"]
for friend_name in my_friends:
	print(f"{friend_name.title()} is one of my friend")
	print(f"wish to meet you soon {friend_name.title()}")
print("take care")
print(my_friends)



for value in range(-11,10):
	print(value)

numbers=list(range(1,10))
print(numbers)
number_skipped=list(range(1,10,3))
even_numbers=list(range(2,20,2))
print(number_skipped)
print(even_numbers)
odd_numbers=list(range(1,20,2))
print(odd_numbers)


squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)

qubes=[]
for values in range(1,20,3) :
	qube=values**3
	qubes.append(qube)
print(qubes)

qubic=[]
for numbers in range(2,11,2):
	qubic.append(numbers**2)
print(qubic)


print(min(qubic))
print(max(squares))
print(sum(even_numbers))

square_list=[value**2 for value in range(1,11)]
print(square_list)

qube_list=[values**3 for values in range(20,41,5)]
print(qube_list)

print(qube_list[1:4])
print(qube_list[:4])
print(qube_list[1:])
print(qube_list[-2:])

#copied_qube_list=qube_list

copied_qube_list=qube_list[:]
print(copied_qube_list)

print(f"list of qube is {qube_list} \ncoppied qube list is {copied_qube_list}")
qube_list.append(" 100000")
copied_qube_list.append("200000")
print(qube_list)
print(copied_qube_list)


#tuples
new_tuple=("1","2","3")
print(new_tuple[1])
for value in new_tuple:
	print(value)
new_tuple=("1","2","3","10")
for value in new_tuple:
	print(value)