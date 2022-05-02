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
    print()

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
    print('the factors of', num, 'are: ')
    factor_list = []
    for i in range(1, num+1):

        if(num % i) == 0:

            print(i, end=' ')
            factor_list.append()

        
    print()
    print("That integer has {} factors". format(len(factor_list)))
    if len(factor_list) == 2:
        print("This is a prime number")

    elif num ==  1:
        print("1 is unity (Only has 1 factor, itself) ")

    
    int_num = int(num)
    root = math.sqrt(int_num)

    if int(root + 0.5) ** 2 == num:
        print(num, 'is a perfect square')

    else:
        print(num, 'is not a perfect square')
        
# Main routine goes here

# Heading
        statement_generator("Factor Calculator", "*")

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

    if var_to_factor !=1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! it only has one factor. Itself"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # generate heading...
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factos of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()

print()
print("Thank you for using the factors calculator")








