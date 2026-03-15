# Simple calculator

# Get input from user
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Error: cannot divide by zero.")
        result = None
    else:
        result = num1 / num2
else:
    print("Invalid operator.")
    result = None

# Show result if calculation succeeded
if result is not None:
    print("Result:", result)