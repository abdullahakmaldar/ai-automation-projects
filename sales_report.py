import csv

input_file = "sales_data.csv"
output_file = "sales_summary.txt"

total_sales = 0
total_items = 0

with open(input_file, newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        quantity = int(row["Quantity"])
        price = int(row["Price"])

        sale = quantity * price

        total_sales += sale
        total_items += quantity

with open(output_file, "w") as file:
    file.write("Sales Summary\n")
    file.write("----------------\n")
    file.write(f"Total Items Sold: {total_items}\n")
    file.write(f"Total Sales Amount: ${total_sales}\n")

print("Report generated successfully")