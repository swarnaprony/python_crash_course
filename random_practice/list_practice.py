#02/03/2020


good_qualities=["trustworthy","helpful","respectful","kind"]
print(good_qualities)
print(good_qualities[2])
print(good_qualities[2].title())
print(good_qualities[-1].upper())
pick_one=f"mostly I like him for his {good_qualities[3]}ness nature"
print(pick_one.title())

good_qualities[3]="very kind"
print(good_qualities[3])
print(good_qualities)
good_qualities.append("strong")
print(good_qualities)

family_members=[]
family_members.append("nirmal")
family_members.append("radha")
family_members.append("supta")

family_members.insert(2,"sumon")
family_members.insert(0,"kamini")
family_members.insert(1,"Rahim")

del family_members[1]
print(family_members)

popped_family_member=family_members.pop()
print(family_members)
print(popped_family_member)

popped_family_members=family_members.pop(2)
print(f"Favourite person in family is {popped_family_members.title()}")

family_members.remove("kamini")
print(family_members)

family_members_again=['kamini', 'nirmal', 'radha', 'sumon', 'supta']
dadu="kamini"
family_members_again.remove("kamini")
print("family_members_again")
print(f"\t{dadu} is our beloved dadu")


family_members_again.sort()
print(family_members_again)
family_members_again.sort(reverse=True)
print(family_members_again)

print(f"Here is the original list: {family_members_again}")
print(f"Here is the sorted list:{sorted(family_members_again)}")
print(f"Here is the original list again: {family_members_again}")

family_members_again.insert(0,"kamini")
family_members_again.reverse()
print(family_members_again)

print(len(family_members_again))