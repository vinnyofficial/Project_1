import math


def factorial(n):
    if n < 0:
        raise ValueError("This program cannot calculate the factorial of a negative number")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def calculator():
    print("YOU HAVE ENTERED NUMBER 2 THAT IS CALCULATOR")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter operator (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed")
            return
    else:
        print("Invalid operator")
        return

    print("Result =", result)


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def advanced_calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Logarithm (base 10)")
        print("11. Natural Logarithm")
        print("12. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12): ")

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", num1 + num2)
            elif choice == '2':
                print(num1, "-", num2, "=", num1 - num2)
            elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)
            elif choice == '4':
                try:
                    print(num1, "/", num2, "=", num1 / num2)
                except ZeroDivisionError:
                    print("Error: Division by zero")
            elif choice == '5':
                print(num1, "^", num2, "=", num1 ** num2)

        elif choice in ('6', '7', '8', '9', '10', '11'):
            num = float(input("Enter a number: "))

            if choice == '6':
                print("Square root of", num, "=", math.sqrt(num))
            elif choice == '7':
                print("Sine of", num, "=", math.sin(math.radians(num)))
            elif choice == '8':
                print("Cosine of", num, "=", math.cos(math.radians(num)))
            elif choice == '9':
                print("Tangent of", num, "=", math.tan(math.radians(num)))
            elif choice == '10':
                print("Logarithm (base 10) of", num, "=", math.log10(num))
            elif choice == '11':
                print("Natural logarithm of", num, "=", math.log(num))

        elif choice == '12':
            print("Exiting Advanced Calculator...")
            break
        else:
            print("Invalid Input")


# -----------------------------------------------------------------------------------------------
while True:
    print('''

█▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▄▄ █▄█  .  ME
█▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄ █▄▀   █▄█ ░█░  .  ME

            1 = Factorial  
            2 = Calculator
            3 = Fahrenheit to Celsius / Celsius to Fahrenheit
            4 = Advanced Calculator
            5 = Exit Program
        ''')
    choice = int(input("Enter a number: "))

    if choice == 1:
        print("YOU HAVE SELECTED NUMBER 1 THAT IS FACTORIAL")
        try:
            num = int(input("Enter a positive number: "))
            result = factorial(num)
            print(f"The factorial of {num} is {result}")
        except ValueError as e:
            print(e)

    elif choice == 2:
        calculator()

    elif choice == 3:
        print("YOU HAVE ENTERED NUMBER 3 THAT IS FAHRENHEIT TO CELSIUS AND CELSIUS TO FAHRENHEIT")
        fahrenheit_temp = int(input("Enter a Fahrenheit temperature: "))
        celsius_temp = int(input("Enter a Celsius temperature: "))

        celsius_result = fahrenheit_to_celsius(fahrenheit_temp)
        fahrenheit_result = celsius_to_fahrenheit(celsius_temp)

        print(f"{fahrenheit_temp}°F is equal to {celsius_result:.2f}°C")
        print(f"{celsius_temp}°C is equal to {fahrenheit_result:.2f}°F")

    elif choice == 4:
        advanced_calculator()

    elif choice == 5:
        print("Exiting......... tata ba-bye")
        break

    else:
        print("Invalid choice. ..Please try again.")
