# Ask user for width and height, loop the program until they
# Enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # Ask the user for a number
            response = float(input(question))
     
            # Check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)
    
        except ValueError:
            print(error)

# Main Routine starts here...

print()
print("Welcome to the fence cost calculator.\n")

loop = ""
while loop == "":
# This part asks the user to input values for width, length and cost / m of fence
    Width = num_check("What is the width?   ")
    print()
    print(f"{Width} m")

    print()
    print()

    Length = num_check("What is the length?   ")
    print(f"{Length} m")

    print()
    print()

    Cost = num_check("What is the cost / m of your fencing?   $")
    print(f"${Cost} / meter")
    print()

# calculation of fence cost
    fence_cost = 2 * (Length+Width) * Cost
# output
    print(f"The total cost of your fence is ${fence_cost}0")
# asks if user wishes to make another calculation
    loop = input("Press <enter> if you wish to make another calculation or exit to quit.")
    print()
    print()
    print()

print("Thank you for using the fence cost calculator V1.0.")