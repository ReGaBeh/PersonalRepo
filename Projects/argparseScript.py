import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("x", help="First number")
    parser.add_argument("y", help="Second number")
    parser.add_argument("--z", help="Operation", choices=["add", "subtract", "multiply", "divide"])

    args = parser.parse_args()

    print("\nFirst number: " + str(args.x), "Second number: " +
          str(args.y), "Operation: " + str(args.z), "\n")

    print("********RESULT********")

    x1 = int(args.x)
    y1 = int(args.y)

    if args.z == "add":
        result = x1 + y1
    elif args.z == "subtract":
        result = x1 - y1
    elif args.z == "multiply":
        result = x1 * y1
    elif args.z == "divide":
        result = x1 / y1
    else:
        if args.z:
            result = "Unsupported operator"

    print(str(result) + "\n")
