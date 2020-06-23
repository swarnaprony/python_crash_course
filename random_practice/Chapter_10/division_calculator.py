#Handaling the zeroDivisionErrorException
#date: 22/06/2020


try:
    print(5/0)
except ZeroDivisionError:
    print("you cannot devide by zero!")


#Using exceptions to prevent Crashes

print("Give me two numbers and I will divide them")
print("Enter 'quit' to quit")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'quit':
        break
    second_number = input("\nSecond Number: ")
    if second_number == 'quit':
        break

    try:
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        print(f" Answer of the division is : {answer}")