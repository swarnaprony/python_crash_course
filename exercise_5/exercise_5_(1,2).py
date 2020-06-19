#exercise_5_(1,2)
#date: 06/03/2020

#exercise_5_1
#conditional_test

car="subaru"
print("is car=='subaru'? I predict true")
print(car=="subaru")

print("\nis car=='audi'? I predict False.")
print(car=='audi')

astu="mine"
print(astu=='mine')
print(astu=='girls')

#exercise_5_2
#conditional_test

astu_name="MirmdAsif"
if astu_name=="MirMdAsif":
    print(astu_name)
else:
    print("Not equal")
if astu_name.lower()=="mirmdasif":
    print(astu_name.lower())
else:
    print("none")

for number in range(-5,15):
    if 10>=number>=5:
        print(number)
    elif 1<=number<=5:
        print(f"{number} is a small number")
    elif number>10:
        print(f"{number} is a large number")
    elif number<0:
        print(f"{number} is a negative number")
for integer in range(10,101):
    if integer%2==0 and 10<=integer<51:
        print(f"even number {integer}")
    elif integer%2!=0 or integer in range (11,100,2):

        print(f"odd number {integer}")

for item in range(1,16):
    number=[1,5,15]
    if item in number:

       print(f"{item} is in list")
    elif item not in number:    
        print(f"{item} is not in list")