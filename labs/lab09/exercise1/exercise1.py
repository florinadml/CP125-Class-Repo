import pandas as pd


def explore_data(filename):
    data = pd.read_csv(filename)
    total_students = len(data)
    subject = ["Math","Science","English"]
    math_average = round(data["Math"].mean(), 1)
    highest_math_student = data.loc(data["Math"].idmax(), "Name")

    return {"total_students:", total_students,
            "subject:", subject ,
            "math_average:", math_average, 
            "highest_math_student :", highest_math_student
    }

result = explore_data("data/students.csv")
print(result)