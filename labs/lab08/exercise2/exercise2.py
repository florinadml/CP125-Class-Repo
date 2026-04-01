# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    file1= open( file1 , "r")
    list1 = file1.read().splitlines()
    file1.close()

    file2 = open( file2 , "r")
    list2 = file2.read().splitlines()
    file2.close()

    combined = set(list1 + list2)

    sorted_name = sorted(combined)

    output = open(output_file, "w")
    for name in sorted_name :
        output.write(name + "\n")
    output.close()

    return len(sorted_name)




  
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
