def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while true:
        choice = input("Enter choice (1/2/3/4): ")
        if input("Enter choice (1/2/3/4): ") in ('1', '2', '3', '4'):
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
        
        if input("Enter choice (1/2/3/4): ") == '1':
            print(f"Result: {add(num1, num2)}")
        elif input("Enter choice (1/2/3/4): ") == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif input("Enter choice (1/2/3/4): ") == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif input("Enter choice (1/2/3/4): ") == '4':
            print(f"Result: {divide(num1, num2)}")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() == 'no':
                break

if __name__ == "__main__":
    calculator()
