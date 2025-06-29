students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
marks = [82, 48, 79, 65, 91]

#1.Create a dictionary using comprehension that pairs each student with their mark.
student_marks = {student: mark for student, mark in zip(students, marks)}
print("Student Marks:", student_marks)
""" 
Student Marks: 
{'Alice': 82, 'Bob': 48, 'Charlie': 79, 'Diana': 65, 'Eve': 91} 

"""

passed_students = {student: mark for student, mark in student_marks.items() if mark >= 70}
print("Passed Students:", passed_students)

""" 
Passed Students: 
{'Alice': 82, 'Charlie': 79, 'Eve': 91}
"""

#3. Use another dictionary comprehension to convert marks into "Pass" or "Fail" using a threshold of 50.
pass_fail = {student: ("Pass" if mark >= 50 else "Fail") for student, mark in student_marks.items()}
print("Pass/Fail:", pass_fail)

""" 
Pass/Fail: 
{'Alice': 'Pass', 'Bob': 'Fail', 'Charlie': 'Pass', 'Diana': 'Pass', 'Eve': 'Pass'}
"""

sentence = "Data science is fun and insightful"
#4. Write a dictionary comprehension that maps each word to its length.
word_lengths = {word: len(word) for word in sentence.split()}
print("Word Lengths:", word_lengths)

"""
Word Lengths:
{'Data': 4, 'science': 7, 'is': 2, 'fun': 3, 'and': 3, 'insightful': 10}
"""