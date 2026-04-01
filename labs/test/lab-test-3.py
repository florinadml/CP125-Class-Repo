import csv
#Function 1
def read_file():
    bmi_file = open("bmi.csv", "r")
    reader = reader.csv(bmi_file)

    next(reader) #skip header

    total = 0 
    count = 0

    for row in reader :
        print(row)
        total += int(row[1])
        count += 1 
    avg = total / count 
    print("Average Height:", avg)

    bmi_file.close()

#Function 2 
def add_file ():
    Gender = input("Enter Gender :")
    Height = input("Enter Height:")
    Weight = input("Enter Weight :")
    BMI = input("Enter BMI :")

    new_data = open("bmi.csv", "a", newline = "")
    writer = csv.writer(new_data)
    writer.writerow([Gender, Height, Weight, BMI])
    new_data.close()

    print("Data added \n")

    data_file = open("bmi.csv", "r")
    reader = csv.reader(data_file)

    for row in reader :
        print (row)
    data_file.close()

read_file()
add_file ()
