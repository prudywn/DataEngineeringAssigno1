#1.Create a list of 5 fruits and print the third fruit.
fruits = ['banana', 'apple', 'orange', 'pear', 'pineapple']
print(fruits[2])

#2.Create a tuple of 3 numbers and print the second number.
numbers = (1, 2, 3)
print(numbers[1])
#Try modifying it. What happens?
""" numbers[1] = 4
print(numbers)
#   ~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment """

#3.Create a dictionary with 3 key-value pairs and print the value of the second key.
person = {'name': 'John', 'age': 25, 'city': 'New York'}
print(person['age']) #result is 25

#4.Create a set from a list with duplicate values.
list1 = [1, 2, 2, 3, 4, 4, 5]

set1 = set(list1)
print(set1) #result is {1, 2, 3, 4, 5}


""" CHALLENGE """
#Takes 5 user inputs 
name1 = input("Enter your name: ")
name2 = input("Enter your name: ")
name3 = input("Enter your name: ")
name4 = input("Enter your name: ")
name5 = input("Enter your name: ")
#and stores them in a list
names = [name1, name2, name3, name4, name5]
#Converts the list into a set and prints the unique values
namesInSet = set(names)
print(namesInSet)
""" result; Enter your name: James
Enter your name: John
Enter your name: Peter
Enter your name: John
Enter your name: Simon
{'John', 'Peter', 'James', 'Simon'} """