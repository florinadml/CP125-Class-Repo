#FLORINA PIDILIS 
# Storing Number in a List

def analyze_numbers():
    numbers = []

    for i in range (1,6):
        num = int(input(f"Enter number{i}:"))
        numbers.append(num)

    #Arrange numbers is ascending
    numbers.sort()

    #Find total numbers and largest numbers
    total = sum(numbers)
    largest = max(numbers)

    return numbers,total,largest

sorted_number, total_number, largest_number = analyze_numbers()

print("Number in ascending order:", sorted_number)
print("Sum of all numbers:", total_number)
print("Largest number:", largest_number)