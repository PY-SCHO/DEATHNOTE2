def addition(num1, num2):
    totaladd = num1 + num2
    return 'total :', totaladd
    
def subtract(num1, num2):
    totalsub = num1 - num2
    return 'total :', totalsub
    
def multiply(num1, num2):
    totalmul = num1 * num2
    return 'total :', totalmul

def divide(num1, num2):
    totaldiv = num1 / num2
    return 'total :', totaldiv
num1 = int(input('enter a number :'))
num2 = int(input('enter a number :'))

operation = str(input('"+","-","*","/": '))

if operation == "+":
    print(addition(num1, num2))
elif operation == "-":
    print(subtract(num1, num2))
elif operation == "*":
    print(multiply(num1, num2))
elif operation == "/":
    print(divide(num1, num2))
else:
    print("error")
    
    
    
    

