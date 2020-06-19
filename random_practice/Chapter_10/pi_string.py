#pi_string
#printing first 50 digits from pi_million_digits.txt
#date: 18/06/2020



file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(len(pi_string))
print(f"{pi_string[:52]}....")

birthday = input('Enter your birthday, in the form mmddyy: ')

if birthday in pi_string:
    print(f"your birthday is in the digits of pi")
else:  
    print(f"your birthday is not in the digits of pi")
