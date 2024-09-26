def calculator():
    print("Please enter number")
    x = float(input())
    
    print("Enter another number")
    y = float(input())
    
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the number of your choice (1-4): ")
    
    if operation == '1':
        result = x + y
        operator = '+'
    elif operation == '2':
        result = x - y
        operator = '-'
    elif operation == '3':
        result = x * y
        operator = '*'
    elif operation == '4':
        if y != 0:
            result = x / y
            operator = '/'
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation selected!"
    
    return f"{x} {operator} {y} = {result}"

# Run the calculator
print(calculator())
