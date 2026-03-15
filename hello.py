num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
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
if result is not None:
    print("Result:", result)