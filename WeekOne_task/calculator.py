def get_numbers():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x, y


def add():
    x, y = get_numbers()
    print("The Sum of two numbers =", x + y)


def subtract():
    x, y = get_numbers()
    print("The difference of two numbers =", x - y)


def multiply():
    x, y = get_numbers()
    print("The product of two numbers =", x * y)


def divide():
    x, y = get_numbers()
    if y == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Questient of two numbers =", x / y)


def calculator():
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add()
    elif choice == "2":
        subtract()
    elif choice == "3":
        multiply()
    elif choice == "4":
        divide()
    elif choice == "5":
        print("Goodbye!")
        return
    else:
        print("Invalid option!")

    calculator()  # run again


calculator()
