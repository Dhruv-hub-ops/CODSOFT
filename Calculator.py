def calculator():
    print("Simple Calculator")
    print("Enter two numbers and an operation to perform: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation (+, -, *, /): ")
    
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation selected. Please choose +, -, *, or /.")

calculator()
