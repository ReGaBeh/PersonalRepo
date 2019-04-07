import argparse  # Importing argparse

if __name__ == "__main__":  # Statement to determine if the file is being run from import or direct
    parser = argparse.ArgumentParser()  # Initialising the parser

    parser.add_argument("x", help="First number")  # Adding the arguments
    parser.add_argument("y", help="Second number")
    parser.add_argument("--z", help="Operation", choices=["add", "subtract", "multiply", "divide"])
# The program takes three arguments: two numbers (positional) and an operator(optional)

    args = parser.parse_args()  # Definining the argument values based on input

    print("\nFirst number: " + str(args.x), "Second number: " +
          str(args.y), "Operation: " + str(args.z), "\n")  # Printing the entered values

    x1 = float(args.x)  # Turning the str type data to float
    y1 = float(args.y)

    if args.z == "add":  # An if/elif(s) statement to determine what to do based on the operator
        result = x1 + y1  # It returns the result of the two numbers based on the operator and
    elif args.z == "subtract":  # adds it to the var "result"
        result = x1 - y1
    elif args.z == "multiply":
        result = x1 * y1
    elif args.z == "divide":
        result = x1 / y1
    else:  # Else statement determines what to do with an operator that isn't specified
        if args.z:  # Determines if result has a value
            result = "Unsupported operator"  # Sets result to the appropriate response
        elif not args.z:  # either "Unsupported operator" or as a blank string
            result = ""
    if result:  # Determines if "result" has data (it should unless the z argument was omitted)
        print("********RESULT********")  # and prints the result (as a string)
        print(str(result) + "\n")
