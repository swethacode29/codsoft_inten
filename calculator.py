def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def main():
    print("Welcome to the simple calculator!")
    
    # Input first number
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    # Input second number
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    # Input operation choice
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    # Perform calculation based on choice
    if choice == '1':
        result = add(num1, num2)
        operation = "addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "division"
    else:
        print("Invalid choice. Please select a valid operation.")
        return
    
    # Display the result
    if isinstance(result, str):
        print(result)
    else:
        print(f"The result of {operation} between {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
