#date: 28/02/2020
#printing full name

#exercise_2_3
#use of f-strings

person_name="Asif"
message="What do you want to eat as a snacks today?"
print(f"Hello {person_name}, {message}")

#exercise_2_4
#use of lower, upper, title method

first_name="mir Md"
middle_name="asif"
last_name="hossain"
full_name=f"{first_name} {middle_name} {last_name}"
print(full_name)
print(full_name.upper())
print(full_name.lower())
print(full_name.title())

#exercise_2_5
#printing quote of someone famous

print('Mir Md Asif Hossain said, "Once you finished a step, Go for the next step." ')

#exercise_2_6
#printing quote of someone famous using variable

person_name_1="Mir Md. Asif Hossain"
person_quote='"Once you finished a step, Go for the next step."'
print(f"{person_name_1} say's {person_quote}")

#exercise_2_7
#use of rstrip, lstrip and strip method

full_name_1="\tMir\tMd\n\tAsif\n\tHossain\t\t"
print(full_name_1)
print(full_name_1.rstrip())
print(full_name_1.lstrip())
print(full_name_1.strip())

