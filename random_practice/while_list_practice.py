#while_list_practice

unconfirmed_list = ['astu','lu','ri','di']
confirmed_list = []
while unconfirmed_list:
    current_user = unconfirmed_list.pop()
    print(f'{current_user} is a current user')
    confirmed_list.append(current_user)
print("\n the following user has been confirmed")
for confirmed_user in confirmed_list:
    print(confirmed_user.title())
print(confirmed_list)
print(unconfirmed_list)

unconfirmed_list = ['astu','lu','astu','ri','di','mummum','astu','astu']
print(unconfirmed_list)
while 'astu' in unconfirmed_list:
    unconfirmed_list.remove('astu')
print(unconfirmed_list)

responses = {}
polling_active = True

while polling_active:
    name = input('write your name: ')
    response = input('which drinks you want to have? ')
    responses[name] = response
    print(f"{name} want to have {response}.")
    repeat = input('would you like to response another one? (yes/no)')
    if repeat == 'no':
        print('thank you for your reaponse')
        polling_active = False
    #for name,response in responses.items():
        #print(f"{name} want to have {response}.")
print(responses)