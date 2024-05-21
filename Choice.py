def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

def modulus(a, b):
    return a % b

def average(a, b):
    return (a + b) / 2

def power(a, b):
    return a ** b

def main():
    num1, num2 = map(int, input("Enter two numbers: ").split())
    choice = int(input("Enter your option: "))

    result = 0
    if choice == 1:
        result = addition(num1, num2)
    elif choice == 2:
        result = subtraction(num1, num2)
    elif choice == 3:
        result = multiplication(num1, num2)
    elif choice == 4:
        result = division(num1, num2)
    elif choice == 5:
        result = modulus(num1, num2)
    elif choice == 6:
        result = average(num1, num2)
    elif choice == 7:
        result = power(num1, num2)
    else:
        print("Invalid choice!")
        return

    if isinstance(result, float):
        print(f"Result = {result:.2f}")
    else:
        print(f"Result = {result}")

if __name__ == "__main__":
    main()
