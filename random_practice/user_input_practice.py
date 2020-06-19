 #user_input_practice
 #date: 17/03/2020

 #while_loop
current_number = 0
while current_number < 14:
    current_number += 1
    if current_number % 2 == 0:
        #print(f"{current_number} is not odd")
        continue
        print('abc')
    print(f"{current_number} is odd")

x=1
while x <= 5:
    print(x)
    x += 1

city_name = 'write the name of the city you visited'
city_name += '\n enter quit when you are finished'

while True:
    city = input(city_name)

    if city == 'quit':
        break
    else:
        print(f" i have visited {city.title()}")

number = 1
while number <= 20:
    print(number)
    number += 2

message = "if you want to quit, write 'quit': "
message += 'or write a message'
message_1 = ''
while message_1 != 'quit':
    message_1 = input(message)
    print(message_1)

message = "if you want to quit, write 'quit': "
message += 'or write a message'
message_1 = ''
while message_1 != 'quit':
    message_1 = input(message)
    if message_1 != 'quit':
        print(message_1)

message = "if you want to quit, write 'quit': "
message += 'or write a message'
message_1 = ''
while message_1 != 'quit':
    message_1 = input(message)
    if message_1 != 'quit':
        print(message_1)
    else:
        print('your program is terminated')


message = "if you want to quit, write 'quit': "
message += 'or write a message'
message_1 = ''
while message_1 != 'quit':
    message_1 = input(message)
    if message_1 != 'quit':
        print(message_1)
        break
    else:
        print('your program is terminated')
print('thank you for using my program')

text = input("tell me something:")
print(text)

name = input('please enter your name: ')
print(f"\nhello {name}!")

message = 'if you tell your name, we can send you a personalize meesage'
message += 'what is your name?'
name = input(message)
print(f"\n{name}")

age = input('How old are you?')
print(age)

if int(age) >= 18:
    print('you are allowed enter to bar')
else:
    print(f"you are {int(age)}. not allowed to enter")


number = input('Write any number you want to know is even or odd: ')
print(f"Your given number is: {number}")
if int(number) % 2 == 0:
    print(f"{int(number)} is an even number")
else:
    print(f"{int(number)} is a odd number")

