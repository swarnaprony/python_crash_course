#exercise_3_(4-7)
#date: 04/03/2020


#exercise_3_4
#list_for_dinner_invitation

invite_them=["lu","ri","di"]
print(f"I am inviting you for today's dinner {invite_them[0]}")
print(f"I am inviting you for today's dinner {invite_them[1]}")
print(f"I am inviting you for today's dinner {invite_them[2]}")

#exercise_3_5
#change_in_list

print(f"{invite_them[1]} cannot make it")
invite_them[1]="radha"

print(f"I am inviting you for today's dinner {invite_them[0]}")
print(f"I am inviting you for today's dinner {invite_them[1]}")
print(f"I am inviting you for today's dinner {invite_them[2]}")

#exercise_3_6
#add_more_guests

print("Found a new bigger table. So I can invite more people")
invite_them.insert(0,"mummum")
invite_them.insert(2,"mummin")
invite_them.append("ri")
print(invite_them)

print(f"I am inviting you for today's dinner {invite_them[0]}")
print(f"I am inviting you for today's dinner {invite_them[1]}")
print(f"I am inviting you for today's dinner {invite_them[2]}")
print(f"I am inviting you for today's dinner {invite_them[3]}")
print(f"I am inviting you for today's dinner {invite_them[5]}")

#exercise_3_7
#shrinking_guest_list

print("I am sorry to say that I have seat for only two people")
popped_lu=invite_them.pop(1)
print(f"I am sorry {popped_lu} I cannot invite you")
popped_ri=invite_them.pop(4)
print(f"I am sorry {popped_ri} I cannot invite you")
popped_di=invite_them.pop(3)
print(f"I am sorry {popped_di} I cannot invite you")
popped_maa=invite_them.pop(2)
print(f"I am sorry {popped_maa} I cannot invite you")
print(invite_them)
print(f"I am glad {invite_them[0]} you are still invited")
print(f"I am glad {invite_them[1]} you are still invited")

del invite_them[0]
del invite_them[0]
print(invite_them)
