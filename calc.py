import numpy as np ### step 1: installed numpy using terminal commands 

##operation functions
class Calculator:
    def add(self, a, b):
        return np.add(a, b)

    def subtract(self, a, b):
        return np.subtract(a, b)

    def multiply(self, a, b):
        return np.multiply(a, b)

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return np.divide(a, b)

    def remainder(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return np.remainder(a, b)
    
    def checker(self, number):
        if number % 2 == 0:
            return "Number is even"
        else: 
            return "Number is odd"
        
# Function that interacts with the user 
#create object
def main():
    calc = Calculator()

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    print("\nChoose an operation:")
    print(" +  for Addition")
    print(" -  for Subtraction")
    print(" *  for Multiplication")
    print(" /  for Division")
    print(" %  for Remainder")
    print ("@ for Chcker")

    op = input("Enter operation symbol: ")

    if op == "+":
        result = calc.add(a, b)
    elif op == "-":
        result = calc.subtract(a, b)
    elif op == "*":
        result = calc.multiply(a, b)
    elif op == "/":
        result = calc.divide(a, b)
    elif op == "%":
        result = calc.remainder(a, b)
    elif op== "@":
        number = float(input("Enter the number you want to check even or odd: "))
        result= calc.checker(number)
        
    else:
        result = "Invalid operation."

    print("\nResult:", result)


main()
