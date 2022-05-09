
# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero and less than 200"

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is less than 200
            if 0 < response < 201:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# Main Routine goes here
keep_going = ""
while keep_going == "":
    print()
    var_integer = num_check("Enter Integer: ")
    print()
    
    
    
 