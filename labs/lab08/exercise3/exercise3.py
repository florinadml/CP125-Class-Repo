# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv
def calculate_order_total(products_file, order_file, output_file):
    
    products = open(products_file, "r")
    products_reader = csv.reader(products)
    prices = {}

    next(products_reader)
    for row in products_reader :
        prices[row[0]] = float(row[2])

    products.close()

    order = open(order_file,"r")
    order_reader = csv.reader(order)

    total_file = open(output_file, "w", newline = "")
    total_file_writter = csv.writer(total_file)

    total_file_writter.writerow(["product_id", "total_cost"])

    next(order_reader)

    grand_total = 0 

    for row in order_reader:
        products_id = row[0]
        quantity = int(row[1])
        
        price = prices[products_id]
        total_cost = price * quantity

        total_file_writter.writerow([products_id, "{:.2f}".format(total_cost)])

        grand_total += total_cost

    order.close()
    total_file.close()

    return grand_total

result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
