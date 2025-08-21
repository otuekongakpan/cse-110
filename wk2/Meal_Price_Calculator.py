# I added drinks and tips to my code!
child_mealp = input ("What is the price of a child's meal? ")
adult_mealp = input ("What is the price of an adult's meal? ")
drinks = input ("What is the price of drinks? ")
count_child = input ("How many children are there? ")
count_adult = input ("How many adults are there? ")
count_drinks = input ("How many drinks were ordered? ")

child_mealp_input = float(child_mealp)
adult_mealp_input = float(adult_mealp)
drinks_input = float(drinks)
count_child_input = int(count_child)
count_adult_input = int(count_adult)
count_drinks_input = int(count_drinks)

print()
subtotal = child_mealp_input * count_child_input + adult_mealp_input * count_adult_input + drinks_input * count_drinks_input

print(f"Subtotal: ${subtotal:.2f}")
print()

sales_taxrate = input ("What is the sales tax rate? ")
sales_taxrate_input = float(sales_taxrate)
sales_tax_amount = (subtotal * sales_taxrate_input / 100)

print(f"Sales Tax: ${sales_tax_amount:.2f}")

tips = input("Tips: ")
tips_input = float(tips)

Total =  sales_tax_amount + subtotal + tips_input

print(f"Total: ${Total:.2f}")
print()

ini_payment = input ("What is the payment amount? ")
ini_payment_input = float(ini_payment)
change = ini_payment_input - Total

print(f"Change: ${change:.2f}")