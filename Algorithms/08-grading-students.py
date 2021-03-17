#region Task
'''
    •Any grade less than 40 is a failing grade.
    
    •If the difference between the grade and the next
    multiple of 5 is less than 3, round grade up to the
    next multiple of 5.

    •If the value of grade is less than 38, no rounding!

    -------------------------------------
Example: 

grade = 84 → rounds up to 85
grade = 29 → do not round!
'''
#endregion


def gradingStudents(grades):
    for i,grade in enumerate(grades):
        sub = (5*(grade//5+1))-grade
        if sub < 3 and grade >= 38:
            grades[i] = 5*(grade//5+1)
    return "\n".join(map(str, grades))
if __name__ == "__main__":

    grades_count = int( input())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip()) 
        grades.append(grades_item)
    result = gradingStudents(grades)
    print(result)