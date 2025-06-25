#Use if, elif, else, and logical operators.
num =int(input('Enter number: '))

if num > 0:
    print('Positive') #Enter number: 4  Positive

elif num < 0:
    print('Negative') #Enter number: -4  Negative

else:
    print('Zero') 
    #Enter number: 0 print(Zero) 

#Create a program that checks if someone is eligible to vote.
age = int(input('Enter your age: '))
if age >= 18:
    print('You can vote') 
    #Enter your age: 18  You can vote

else:
    print('Go back home')

while True:
    num1 = int(input('First number: '))
    num2 = int(input('Second Number: '))
    num3 = int(input('Third Number: '))
    if num1 > num2:
        if num1 > num3:
            print(f'Greatest number = {num1}')
        break
    elif num3 > num1:
        if num3 > num2:
            print(f'Greatest number is {num3}')
        break
    else:
        print(f'Greatest number is {num2}')
        break

fruit1 = input('Fruit(1): ')
fruit2 = input('Fruit(2): ')
if fruit1 == 'banana' and fruit2 == 'apple':
    print('Healthy')
elif fruit1 == 'apple' or fruit2 == 'pinneaple':
    print('Still Healthy')

    """ Challenge
Build a grading system:

Input score (0–100)
Output grade: A (90+), B (80–89), etc.
 """
    
score = int(input('Enter the marks you scored(0-100): '))
if score >= 90:
    print('A')
elif score >= 80 and score <= 89:
    print('B')
elif score >= 70 and score <= 79:
    print('C')
elif score >= 60 and score <= 69:
    print('D+')
elif score >= 50 and score <= 59:
    print('D')
else:
    print('F')