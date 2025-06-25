#Check the data type of the following values:
#42
#3.14
#'hello'
#True

print(type(42))
print(type(3.14))
print(type('hello'))
print(type(True))

#Convert a string '100' to an integer.
no_string = '100'
int_value = int(no_string)
print(type(no_string))
print(type(int_value))

#Add an integer and a float together. What is the result?
num1 = 10
num2 = 3.14
num3 = num1 + num2
print(num3)
#result = float

#What happens when you try to multiply a string by a number?
string = "Hello"
num = 5
result = string * num
print(result)
#the result is the string repeated x times

""" CHALLENGE 
Write a program that:

Asks the user to enter two numbers (as strings)
Converts them to integers or floats
Prints their sum and type
"""

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
sum = int(number1) + int(number2)
print(sum)
print(type(sum))