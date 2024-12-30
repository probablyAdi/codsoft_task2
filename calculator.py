print("Simple Calculator")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (1/2/3/4): ")

if operation == '1':
    result = num1 + num2
    print("Result:", result)
elif operation == '2':
    result = num1 - num2
    print("Result:", result)
elif operation == '3':
    result = num1 * num2
    print("Result:", result)
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")