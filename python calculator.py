import math

while True:
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (^)")
    print("7. Square Root (√)")
    print("8. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if choice == '8':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        elif choice == '6':
            result = num1 ** num2
            print(f"{num1} ^ {num2} = {result}")

    elif choice == '7':
        try:
            num = float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if num < 0:
            print("Error! Square root of negative number is not defined.")
        else:
            result = math.sqrt(num)
            print(f"√{num} = {result}")

    else:
        print("Invalid input. Please enter a valid choice.")