import csv

def calculate_final_grades(input_file, output_file):
   total = 0 

   input = open(input_file, "r", newline = "")
   input_reader = csv.reader(input)

   header = next(input_reader)

   for row in input_reader :
      
      student_id = row[0]
      midterm = float(row[1])
      final= float(row[2])

      final_grade = (midterm * 0.4 ) + (final * 0.6 )

      final_grades.([student_id, f"{final_grade :.2f}"])
      total += final_grade 

      input.close()

      output = open(output_file, "w", newline = "")
      output_writer = csv.writer(output)
      output_writer.writerow(["student_id", "final_grade"])

      for row in final_grades :
         output_writer.writerow(row)
      output.close()
      
      if len(final_grades) > 0 :
         average = total / len(final_grades)
      else:
        average = 0
      return average 


result = calculate_final_grades("labs/lab08/exercise4/data/scores.csv", "labs/lab08/exercise4/data/grades.csv")
print(f"Average final grade: {result:.2f}")
