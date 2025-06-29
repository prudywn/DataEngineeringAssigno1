scores = [45, 78, 88, 56, 90, 62, 33, 99, 70, 50]

passed_scores = [score for score in scores if score >= 60]

print("Scores:", scores)
print("Passed Scores:", passed_scores)
""" 
 Output: Scores: [45, 78, 88, 56, 90, 62, 33, 99, 70, 50]
Passed Scores: [78, 88, 90, 62, 99, 70] """
#2. Use another list comprehension to convert all scores into "Pass" or "Fail" using a threshold of 50.
pass_fail = ["Pass" if score >= 60 else "Fail" for score in scores]
print("Pass/Fail:", pass_fail)
"""
    Output: Pass/Fail: ['Fail', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail']
"""