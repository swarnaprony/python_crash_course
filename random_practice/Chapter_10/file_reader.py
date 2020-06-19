with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(len(contents))
    print(f"{contents.rstrip()}")



file_path = 'C:/Users/asifhossain/Documents/python_work/random_practice/text_file/pi_digit_file.txt'
with open(file_path) as new_file_object:
    new_contents = new_file_object.read()
    print(new_contents)

print(f"printing file in line")
with open(file_path) as newest_file_object:
    for line in newest_file_object:
        print(line.rstrip())
        #print(line.rstrip())

with open(file_path) as newest_file_object_2:
    lines = newest_file_object_2.readlines()

pi_string = ''
for line in lines:
    #pi_string += line.rstrip()
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))