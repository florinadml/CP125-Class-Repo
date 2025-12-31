#FLORINA PIDILIS # CHECK GRADE FOR ONE STUDENT
grade = 0
def determine_grade(mark):
    if mark >= 80 :
        grade = "A"
    elif mark >=60 and mark <= 79 : 
       grade = "B"
    elif mark >=50 and mark <=59 :
        grade = "C"
    elif mark >=40 and mark <=49 :
        grade = "D"
    else:
        grade = "F"

    return grade
    
mark = float(input("Enter the student's mark:"))
result = determine_grade(72)
print("Mark:", mark, "Grade:", grade)


