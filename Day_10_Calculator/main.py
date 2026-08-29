import art
import os
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    num1 = int(input("What is the first number?: "))
    starter = 1
    while starter:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's next number?: "))

        result = operations[operation_symbol](num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {result} ")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if choice == "n":
            starter = 0
            os.system('clear')
            print(art.logo)
            calculator()

        elif choice == "y":
            num1 = result

calculator()