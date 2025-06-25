
#Create a function add(a, b) that returns the sum.
def add(a, b):
    return a+b

result = add(9, 5)
print(result, end=' = ') #14

#Modify add() to print “even” or “odd” based on the result.
if result % 2 == 0:
    print('even')
else:
    print('odd') 
#output => 14 => 14 = even

def greet(name):
    age = add(9,10)
    print(f'Hello, {name}.You are turning {age} years old')

greet('Mary') #Output = Hello, Mary

""" Challenge
Write a calculator function:

Takes two numbers and an operation (+, -, *, /)
Returns the result
 """

def calculator(num1, num2,operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
   
result2 = calculator(8, 4, '*')
print(result2) #32
    
    