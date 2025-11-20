def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y


def calculator():
    print("Simple Calculator")
    print("-" * 30)
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("-" * 30)

    while True:
        choice = input("\nEnter operation (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    print(f"\n{num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"\n{num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"\n{num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}")

            except ValueError:
                print("Error: Please enter valid numbers")
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    calculator()