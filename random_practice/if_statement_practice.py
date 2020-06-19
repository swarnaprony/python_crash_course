#date: 06/03/2020
#practicing_if_statement

cars=["tesla","marcedes","toyota","bmw","hondai"]

for car in cars:
    if car.lower()=="bmw":
        print(car.upper())
    else:
        print(car.title())

for car in cars:
    if car!="bmw":
        print(car.title())
    else:
        print(car.upper())
odd=15
if odd<10 or odd>10:
    print(odd)
else:
    print(f"{odd} equal 10")  

if "corolla" not in cars:
    print(f"corolla does not belomg to the cars list")

if "bmw" in cars:
    print(f"bmw does belong to the cars list")

car="subaru"
print("is car=='subaru'? I predict true")
print(car=="subaru")

print("\nis car=='audi'? I predict False.")
print(car=='audi')

asif_age=30
print(asif_age==3)
print(asif_age==30)

persons_age=15
if persons_age<=10:
    print("is a child")
    print("can participate at sports competetion")
else:
    print("not a child")
    print("cannot participate at sports competetion")

age=15
if age<4:
    print("admission is free")
elif 4<=age<=18:
    print("admission fee is $25")
else:
    print("admission fee is $40")

for age in range(0,57):
    if age<4:
        price="none"
    elif 4<=age<=18:
        price=25
    elif 18<=age<=50:
        price=40
    else:
        price=30
    print(f"price is {price}")

requested_toppings=["olive","pinapple","mashroom","cheese"]
if "olive" in requested_toppings:
    print("add olive") 
if "carrot" in requested_toppings:
    print("add carrot")
if "cheese" in requested_toppings:
    print("add cheese")
print("finished")  

for requested_topping in requested_toppings:
    if requested_topping=="olive":
        print(f"Sorry we are out of {requested_topping}")
    if requested_topping=="cheese":
        print(f"do you need any extra {requested_topping}")
    else:
        print(f"add {requested_topping}")
print("pizza is ready")

requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping=="olive":
            print(f"Sorry we are out of {requested_topping}")
        if requested_topping=="cheese":
            print(f"do you need any extra {requested_topping}")
        else:
            print(f"add {requested_topping}")
    print("pizza is ready")
else:
    print("are you sure want a plain pizza?")

available_toppings=["olive","pinapple","mashroom","cheese","green peeper","pepperoni"]
requested_toppings=["french fries","olive","cheese"]
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"add {requested_topping}")
        else:
            print(f"Sorry we are out of {requested_topping}")
    print("pizza is ready")
else:
    print("are you sure want a plain pizza?")