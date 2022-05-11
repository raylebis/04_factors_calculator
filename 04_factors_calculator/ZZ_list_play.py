import random

def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero and less than 200"

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is less than 200
            if response < 201:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# set up a list

my_list = [2, 0, 9, 8, 7]

# generate 4 random numbers between 1 and 10...
for item in range(0,4):

    # generate random number between 1 and 10
    random_num = random.randint(1, 10)

    # add number to list
    my_list.append(random_num)

# print the unsorted list...
print(my_list)

# sort the list
my_list.sort()

my_list_len = len(my_list)

# print the sorted list
print()
print(my_list)
print("The list has {} items".formate(my_list_len))
print()

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
