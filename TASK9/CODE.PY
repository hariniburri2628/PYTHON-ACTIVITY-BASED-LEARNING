budget = float(input("Enter travel budget in INR: "))

fee_rate = float(input("Enter conversion fee percentage: "))

n = int(input("Enter number of expenses: "))

expenses = {}
total_spending = 0

for i in range(n):

    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency code: ").upper()
    exchange_rate = float(input("Enter exchange rate to INR: "))

   
    if amount < 0 or exchange_rate <= 0:
        print("Invalid expense details!")
        continue

    converted_amount = amount * exchange_rate
   
    conversion_fee = converted_amount * fee_rate / 100
    
    final_amount = converted_amount + conversion_fee

    total_spending += final_amount
    expenses[category] = expenses.get(category, 0) + final_amount

    print("Currency:", currency)
    print("Converted Amount: Rs.", round(converted_amount, 2))
    print("Conversion Fee: Rs.", round(conversion_fee, 2))
    print("Total Expense: Rs.", round(final_amount, 2))
print("\n===== TRAVEL BUDGET REPORT =====")

print("Planned Budget: Rs.", round(budget, 2))
print("Total Spending: Rs.", round(total_spending, 2))

if total_spending > budget:
    print("Budget Status: Budget Exceeded")
else:
    print("Budget Status: Within Budget")

remaining = budget - total_spending

print("Remaining Budget: Rs.", round(remaining, 2))

if expenses:

    largest_category = max(expenses, key=expenses.get)

    print("\nLargest Expense Category:", largest_category)

    print("Expense Details:")

    for category, amount in expenses.items():
        print(category, ": Rs.", round(amount, 2))

else:
    print("No valid expenses entered.")

print("\nTravel budget analysis completed.")

