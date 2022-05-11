
import math



def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)

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
            if 0 < response < 201:
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
    factor_list = []
    for i in range(1, num+1):

        if(num % i) == 0:

            print(i, end=' ')
            factor_list.append(i)

            factor_list.sort
        
    print()
    print("That integer has {} factors". format(len(factor_list)))
    if len(factor_list) == 2:
        print(num, 'is a prime number')

    elif num ==  1:
        print("1 is unity (Only has 1 factor, itself) ")

    # Perfect square finder
    
    int_num = int(num)
    root = math.sqrt(int_num)

    if int(root + 0.5) ** 2 == num:
        print(num, 'is a perfect square')
    else:
        print(num, 'is not a perfect square')
        
    return factor_list


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
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()
