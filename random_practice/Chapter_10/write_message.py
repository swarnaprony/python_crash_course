#writing text to a file through programming
#date: 18/06/2020

file_name = 'programming.txt'

with open(file_name, 'w') as new_file_object:
    new_file_object.write("I love programming with Python. \n")
    new_file_object.write("I am learning Python for Data analysis.\n")

with open(file_name, 'a') as file_object:
    file_object.write("I like finding meaning in large dataset. \n")


file_name_1 = 'programming.txt'
with open(file_name_1, 'r+') as new_file_object_1:
    lines = new_file_object_1.read()
    print(lines)

    new_file_object_1.write("I am learning Python rigorously.")

file_name_2 = 'pi_million_digits.txt'


new_digits = ''
with open(file_name_2, 'r') as new_file_object_2:
    digit = new_file_object_2.read()
    new_digits += digit

file_name_3 = 'pi_digits.txt'

with open(file_name_3, 'a') as new_file_object_3:
    new_file_object_3.write(new_digits)


