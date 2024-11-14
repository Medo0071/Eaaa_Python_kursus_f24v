def hello_world(name):
    print("Hello " + name)

def calculator():
    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")

    choice = input("Enter choice(Addition/Subtraction/Multiplication/Division): ")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == 'Addition':
        print(num1 + num2)

    elif choice == 'Subtraction':
        print(num1 - num2)

    elif choice == 'Multiplication':
        print(num1 * num2)

    elif choice == 'Division':
        print(num1 / num2)

    else:
        print("Invalid input")


calculator()


