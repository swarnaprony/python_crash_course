#exercise_10_5
#programming_poll
#date: 19/06/2020


responer_name = "write your name: "
user_response = "write down the reason why you like programming: "
getting_out = "If you finished with it write 'quit' or 'no': "

user_name_entry = ''
user_response_entry = ''
getting_out_entry = ''

while getting_out_entry != 'quit':
    response_list = 'user_response.txt'
    with open(response_list, 'a') as user_response_object:
        getting_out_entry = input(getting_out)

        if getting_out_entry != 'quit':
            user_name_entry = input(responer_name)
            user_response_entry = input(user_response)

            user_response_object.write(f"{user_name_entry} \n")
            user_response_object.write(f"{user_response_entry}. \n")

        else:
            print("Thanks for your response")
