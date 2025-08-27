# Basic Calculator Program
# Week 1 Assignment

# Simple Calculator using a Dictionary

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get the operation from the user
operation = input("Enter the operation (+, -, *, /): ")

# Dictionary of operations
operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2 if num2 != 0 else "Error (division by zero)"
}

# Show the result if the operation is valid
if operation in operations:
    result = operations[operation]

    # Remove .0 for whole numbers
    if isinstance(result, (int, float)) and result == int(result):
        result = int(result)
    if num1 == int(num1):
        num1 = int(num1)
    if num2 == int(num2):
        num2 = int(num2)

    print(f"{num1} {operation} {num2} = {result}")
else:
    print("Invalid operation")

Enter the first number: 10
Enter the second number: 5
Enter the operation (+, -, *, /): +
10 + 5 = 15
