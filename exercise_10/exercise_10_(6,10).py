#exercise_10_(6,10)
#date: 23/06/2020


#exercise_10_6,7
#Addition_excepting_value_error
#Addition_Calculator
#Using_while-loop

def adding_number():
    """adding two integer with handling error"""
    quit_program = ''
    while quit_program != 'quit':

        try:

            quit_program = input(" If you want to quit the program write: 'quit' or 'no'\n")
            number_1 = input("Write down the first number: \n")
            number_2 = input("Write down the second number: \n")
            answer = int(number_1) + int(number_2)
            print(answer)
        except ValueError:
            print("Please insert an Integer Number")
adding_number()



