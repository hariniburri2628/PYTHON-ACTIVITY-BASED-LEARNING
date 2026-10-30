

def calculate_bill(units):
    
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + ((units - 100) * 3)

    else:
        energy_charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)
    
    fixed_charge = 50
 
    surcharge = energy_charge * 0.05
    rebate = 0

    if units < 100:
        rebate = energy_charge * 0.10

    
    total_bill = energy_charge + fixed_charge + surcharge - rebate

    return round(total_bill, 2)

n = int(input("Enter number of months: "))

bills = []

for i in range(n):

    print("\nMonth", i + 1)

    units = float(input("Enter electricity units consumed: "))

    bill = calculate_bill(units)

    bills.append(bill)

    print("Electricity Bill: Rs.", bill)


print("\n===== MONTHLY BILL COMPARISON =====")

for i in range(n):

    print("Month", i + 1, ": Rs.", bills[i])

    if i > 0:

        increase = bills[i] - bills[i - 1]

        if bills[i - 1] > 0:
            percentage = (increase / bills[i - 1]) * 100

            if percentage > 30:
                print("Warning: Unusual increase detected!")
            else:
                print("Bill is normal.")

        elif bills[i] > 0:
            print("Warning: Bill increased from zero.")

print("\nBilling process completed.")

