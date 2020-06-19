#exercise_5_(8,11)
#date: 11/03/2020
#for_if

#exercise_5_8
#hello_admin

usernames = ["secretary","staff","analyst","programer","admin"]
for username in usernames:
    if username == "admin":
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}. Welcome to the meeting")

#exercise_5_9
#no_users

usernames = ["staff","analyst","programer","admin"]
if usernames:
    for username in usernames:
        if username == "admin":
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}. Welcome to the meeting")
else:
    print("we need to find new user")

users=["staff","analyst","programer","admin"]
for i in range(0,4):
    print(f"{users[0]} is removed from the list in loop")
    del users[0]
print(f"{users} is an empty list") 

#exercise_5_10
#checking_username

current_users_upper = ["ri","lu","di","astu","tom","Zeejun","zeeja"]
current_users = []
for user in current_users_upper:
    current_users.append(user.lower())
print(current_users)
new_users = ["maa","bapi","Di","zeejun","mummum","mummin"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} username is alreay in the list. need to enter a new username")
    else:
        print(f"{new_user} username is available")

#exercise_5_11
#ordinal_numbers
numbers=[]
for number in range(1,10):
    numbers.append(number)
print(numbers)
for item in numbers:
    if item == 1:
        print(f"{item}st")
    elif item == 2:
        print(f"{item}nd")
    elif item == 3:
        print(f"{item}rd")
    else:
        print(f"{item}th")

