'''
HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

- If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
- If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

- Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

'''

def gradingStudents(grades):
    # Write your code here
    #print("=======",grades)
    new_grades=[] 
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
        else:
            if (grade+2)%5==0:
                new_grades.append(grade+2)
            elif (grade+1)%5==0:
                new_grades.append(grade+1)
            else:
                new_grades.append(grade)
    return new_grades