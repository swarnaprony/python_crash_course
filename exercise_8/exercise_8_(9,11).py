#exercise_8_(9,11)
#date: 02/04/2020

#exercise_8_9
#messages

def show_message(messages):
    for message in messages:
        print(message)
short_text = ['good morning', 'good noon', 'good evening', 'good night']
show_message(short_text)

#exercise_8_10
#sending_messages

def send_message(send_messages,sent_messages):
    while send_messages:
        send_message = send_messages.pop()
        print(f"you should send this message: {send_message}")
        sent_messages.append(send_message)
def sent_message(sent_messages):
    for message in sent_messages:
        print(f"you have sented the message: {message}")
send_messages = ['good morning', 'good noon', 'good evening', 'good night']
sent_messages = []
send_message(send_messages,sent_messages)
sent_message(sent_messages)

#exercise_8_11
#archived_messages

def send_message(send_messages,sent_messages):
    while send_messages:
        send_message = send_messages.pop()
        print(f"you should send this message: {send_message}")
        sent_messages.append(send_message)
def sent_message(sent_messages):
    for message in sent_messages:
        print(f"you have sented the message: {message}")
send_messages = ['good morning', 'good noon', 'good evening', 'good night']
sent_messages = []
send_message(send_messages[:],sent_messages)
sent_message(sent_messages)
print(send_messages)

