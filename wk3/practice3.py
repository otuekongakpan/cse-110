"""
Grade Evaluator

By

Otuekong Akpan
"""

grade = int(input("What is your score for this term? "))

if grade >= 90:
    print("Grade: A (Excellent!)")
elif grade >= 80:
    print("Grade: B (Good job!)")
elif grade >= 70:
    print("Grade: C (You Passed!)")
elif grade >= 60:
    print("Grade: D (Needs improvement.)")
else:
    print("Grade: F (Failed. Try harder next time!)") 