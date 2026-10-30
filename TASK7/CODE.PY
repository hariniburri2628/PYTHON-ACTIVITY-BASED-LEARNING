products = []

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0
tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "grocery": 2
}

for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category: ").lower()
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    if category not in tax_rates or price < 0 or quantity <= 0:
        print("Invalid product details!")
        continue
    amount = price * quantity
    tax = amount * tax_rates[category] / 100

    subtotal += amount
    total_tax += tax

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "amount": amount,
        "tax": tax
    })

if subtotal > 10000:
    discount = subtotal * 0.15

elif subtotal > 5000:
    discount = subtotal * 0.10

else:
    discount = 0

discount = min(discount, 2000)

final_bill = subtotal + total_tax - discount

print("\n========== RETAIL INVOICE ==========")

print("\nProduct       Category    Qty    Amount    Tax")

for p in products:

    print(
        p["name"],
        p["category"],
        p["quantity"],
        round(p["amount"], 2),
        round(p["tax"], 2)
    )

print("------------------------------------")
print("Subtotal       : Rs.", round(subtotal, 2))
print("Total Tax      : Rs.", round(total_tax, 2))
print("Discount       : Rs.", round(discount, 2))
print("------------------------------------")
print("Final Bill     : Rs.", round(final_bill, 2))
print("====================================")
print("Thank you for shopping!")

       

