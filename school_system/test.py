def generate_enrollment_report(old_file, new_file, output_file):
    f = open(input_file,'r')
    total = len(f.readlines())

    f.close()

    f = open(output_file,'w')
    f.write(f'Total Students {total}')
    f.close()

    count_students("students/2024/names.txt", "report/sumarytext")


import csv
def check_low_attendance(input_file, output_file, threshold):
    f = open(input_file, 'r',newline="")
    reader = csv.DictReader(f)
    
    header = next(reader)

    

    result = []
    for line in reader:
        if line[1] < threshold:
            result.append(line[0])

    
    f = open(output_file, 'w') 
    for student in low_attendance_students:
        f.write(student + "\n")
    f.close()
    
    