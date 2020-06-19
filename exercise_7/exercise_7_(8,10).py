#exercise_7_(8,10)
#date: 20/03/2020

#exercise_7_8
#deli

sandwich_order = ['chessee','chicken','vegetable','vegan']
order_completed = []
while sandwich_order:
    order = sandwich_order.pop()
    print(order)
    order_completed.append(order)
print(order_completed)

sandwich_order = ['chessee','chicken','vegetable','vegan']
order_completed = []
for sandwich in sandwich_order:
    order = sandwich_order.pop()
    print(order)
    order_completed.append(order)
print(order_completed)

#exercise_7_9
#no_pastrami

sandwich_order_1 = ['pastrami','chessee','chicken','pastrami','vegetable',
'vegan','pastrami']
order_completed_1 = []
while sandwich_order_1:
    order = sandwich_order_1.pop()
    print(order)
    if order == 'pastrami':
        print('we are out of pastrami')
    else:
        order_completed_1.append(order)
print(order_completed_1)
print('your sandwich is ready')

#exercise_7_10
#dream_vacation

active_polling = True
while active_polling:
    name = input('write your name: ')
    place_name = input('write a name of the place you want to visit: ')
    print(f"{name} want to visit {place_name}")
    leave = input('if you want to quit write "quit" otherwise "no"')
    if leave == 'quit':
        break
