#exercise_5_(3,7)
#date: 10/03/2020
#if_elif_else

#exercise_5_3
#allien_colour

colour = "red"
if colour == "green":
    print("the player just earned 5 points")

if colour == "red":
    print("the player just earned 5 points")


#exercise_5_4
#allien_colour

colour = "red"
if colour == "green":
    print("the player just earned 5 points")
if colour != "green":
    print("the player just earned 10 points")

colour = "yellow"
if colour == "green":
    print("the player just earned 5 points")
else:
    print("the player just earned 15 points")

#exercise_5_5
#allien_colour

colour = "yellow"
if colour == "green":
    print("the player just earned 5 points")
elif colour == "red":
    print("the player just earned 10 points")
else:
    print("the player just earned 15 points")

colour = "green"
if colour == "green":
    print("the player just earned 5 points")
elif colour == "red":
    print("the player just earned 10 points")
else:
    print("the player just earned 15 points")

colour = "red"
if colour == "green":
    print("the player just earned 5 points")
elif colour == "red":
    print("the player just earned 10 points")
else:
    print("the player just earned 15 points")

#exercise_5_6
#stages_of_life

age_is = 1
if age_is < 2:
    print("person is a baby")
elif 2 <= age_is < 4:
    print("person is a todler")
elif 4 <= age_is < 13:
    print("person is a kid")
elif 13 <= age_is < 20:
    print("person is a teenager")
elif 20 <= age_is < 65:
    print("person is a adult")
elif age_is >= 65:
    print("person is a elder")

#exercise_5_7
#favourite_fruit

favourite_fruits = ["lichi","mango","jam","jackfruit"]
if "banana" in favourite_fruits:
    print(f"banana is one of my favourite_fruits")
if "mango" in favourite_fruits:
    print(f"mango is one of my favourite_fruits")
if "apple" in favourite_fruits:
    print(f"apple is one of my favourite_fruits")
if "jackfruit" in favourite_fruits:
    print(f"jackfruit is one of my favourite_fruits")
if "jam" in favourite_fruits:
    print(f"jam is one of my favourite_fruits")
