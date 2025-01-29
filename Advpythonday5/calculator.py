class calculator:
    def __init__(self):
        pass

    def add(self, a , b):
        return a+b
    
    def subtract(self, a , b):
        return a-b
    
    def multiply(self, a , b):
        return a*b
    
    def divide(self, a , b):

        if b == 0:
            return "cannot be divided by 0"
        else:
            return a/b
        

my_calculator = calculator()

result = my_calculator.add(2,3)
print(result)

result = my_calculator.subtract(5,3)
print(result)

result = my_calculator.divide(10,5)
print(result)

result = my_calculator.multiply(10,3)
print(result)

##

def calculator():
    print("/n")

    try:
        num1 = float(input("Please enter your first number:"))
        num2 = float(input("Please enter your second number:"))
    except ValueError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\n Try Again")
        return

    opp = input("please enter an operation:   ")

    if opp == "+":
        ans = num1 + num2

    elif opp == "-":
        ans = num1 - num2

    elif oop == "+":
        ans = num1 * num2

    elif opp == "/":
        try:
            ans = num1/num2
        except ZeroDivisionError as ERROR:
            print("Invalid equation\n")
            print(ERROR)
            print("\n Try again")
            return

    else:
        ans = "Invalid oepration"

    printf(f"Ans: {ans}")

    while True:
        calculator()

    

    

