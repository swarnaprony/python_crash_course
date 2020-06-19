#exercise_10_3
#guest

user_name = input('Write your name here: ')

user_name_file = 'guest.txt'

with open(user_name_file, 'a') as user_name_object:
    user_name_object.write(f"{user_name}\n")


#exercise_10_4
#guest_book



user_name_entry = "Enter your name: "
user_name_entry += "if ypu finished with adding name write 'quit' to get out: "

guest_user = ''

while guest_user != 'quit':
    guest_user_list = 'guest_user_name_list.txt'
    with open(guest_user_list, 'a') as guest_user_object_all:

        if guest_user != 'quit':
            guest_user = input(user_name_entry)

            guest_user_object_all.write(f"{guest_user}\n")
            guest_user_object_all.write(f"Thanks for visiting us {guest_user}. \n")
        else:
            print('List is ready')


