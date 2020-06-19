#exercise_7_(4,7)
#date: 19/03/2020

#exercise_7_4
#pizza_toppings

pizza_toppings = "write the name of the topping you want in your pizza: "
pizza_toppings += "\n if you finished with adding write 'quit' to get out: "
pizza_topping = ''

while pizza_topping != 'quit':
    pizza_topping = input(pizza_toppings)
    print(f" add {pizza_topping}")
print("your pizza is ready")

#exercise_7_5
#movie_tickets

persons_age = 'write your age: '
quit_program = 'if you want to exit write "quit" otherwise "no": '

while True:
    person_age = int(input(persons_age))

    if 0 < person_age < 3:
        print('ticket is free')
    elif 3 <= person_age <= 12:
        print('ticket price is 10')
    elif person_age >12:
        print('ticket price is 15')
    else:
        print('you have to give a valid age')

    quits_program = input(quit_program)
    if quits_program == 'quit':
        print("program is terminated")
        break

#exercise_7_6
#date: 19/03/2020


pizza_toppings = "write the name of the topping you want in your pizza: "
pizza_toppings += "\n if you finished with adding write 'quit' to get out: "
pizza_topping = ''
activate_variable = 1 

while activate_variable <= 3:
    pizza_topping = input(pizza_toppings)
    print(f" add {pizza_topping}")
    activate_variable += 1
print("your pizza is ready")


pizza_toppings = "write the name of the topping you want in your pizza: "
pizza_toppings += "\n if you finished with adding write 'quit' to get out: "
pizza_topping = ''

while True:
    pizza_topping = input(pizza_toppings)
    print(f" add {pizza_topping}")
    if pizza_topping == 'quit':
        print('terminated')
        break
print("your pizza is ready")

#exercise_7_7:
#infinity

while True:
    print('I love you astu')
 