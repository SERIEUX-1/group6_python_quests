#!/usr/bin/python3
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return "Error: can not be divided by zero"
    return x/y
number1 = int( input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("Enter the operation (add,sub,mul,div): ")
if operation == "add":
    result = add(number1,number2)
elif operation == "sub":
    result = sub(number1,number2)
elif operation == "mul":
    result = mul(number1,number2)
elif operation == "div":
    result = div(number1,number2)
else:
    result = "Incorrect operation"
print(f"Result = {result}")
