# Functions go here

# Puts series of symbols at start and end of text
import math


def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)


    print()
    print(statement)

    return ""

# displays instructions / information
def instructions():

    print()
    print("Please choose a number that is less than 200 or more than 1")
    print()
    print("This program finds the factors of the given integers and states if the number is a prime or a perfect square")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    return ""

# checks input is a number more than a given value
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero and less than 200"

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response < 201:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# gets factors, returns a sorted list    
def get_factors(num):
    print('The factors of', num, 'are: ')
    print()
    factor_list = []
    for i in range(1, num+1):

        if(num % i) == 0:

            print(i, end=' ')
            factor_list.append(i)

            factor_list.sort
        

# Main routine goes here

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue: ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number: ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! it only has one factor. Itself"

    int_num = int(var_to_factor)
    root = math.sqrt(var_to_factor)

    if factor_list == 2:
        comment = var_to_factor, 'is a prime number'

    if int (root + 0.5) ** 2 == var_to_factor:
        comment = ("{} is a perfect square".format(var_to_factor))
    else:
        comment = ("{} is not a perfect square".format(var_to_factor))

    # generate heading...
    if var_to_factor == 1:
        comment = "One is UNITY! it only has one factor. Itself"
    else:
        comment = ""

    # Output factors and comment
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()

print()
print("Thank you for using the factors calculator")








