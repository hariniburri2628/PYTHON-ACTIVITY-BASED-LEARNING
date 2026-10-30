# Progressive Electricity Billing System Using Python

## 1. Problem Statement

The Progressive Electricity Billing System calculates household electricity bills based on monthly electricity consumption using multiple consumption slabs, fixed charges, surcharges, and rebates.

The system accepts electricity consumption details for several months, calculates the final bill for each month, and compares the bills to identify unusual increases. If the current month's bill increases by more than 30% compared to the previous month, the system displays an unusual increase warning.

## 2. Algorithm

1. Start the program.
2. Enter the number of months.
3. Enter electricity consumption in units for each month.
4. Calculate electricity charges using progressive slabs:
   - First 100 units: ₹2 per unit.
   - Next 100 units: ₹3 per unit.
   - Above 200 units: ₹5 per unit.
5. Add fixed charges of ₹50.
6. Calculate a 5% surcharge on energy charges.
7. Apply a 10% rebate on energy charges if consumption is below 100 units.
8. Calculate the final electricity bill.
9. Store all monthly bills.
10. Compare each month's bill with the previous month's bill.
11. If the increase is greater than 30%, display an unusual increase warning.
12. Display all monthly bills and warnings.
13. Stop the program.

## 3. Flowchart


## 5. Sample Input


Enter number of months: 4

Month 1
Enter electricity units consumed: 80

Month 2
Enter electricity units consumed: 120

Month 3
Enter electricity units consumed: 180

Month 4
Enter electricity units consumed: 250


## 6. Sample Output


Month 1
Electricity Bill: Rs. 209.6

Month 2
Electricity Bill: Rs. 417.5

Month 3
Electricity Bill: Rs. 606.5

Month 4
Electricity Bill: Rs. 1032.5

===== MONTHLY BILL COMPARISON =====

Month 1 : Rs. 209.6

Month 2 : Rs. 417.5
Warning: Unusual increase detected!

Month 3 : Rs. 606.5
Bill is normal.

Month 4 : Rs. 1032.5
Warning: Unusual increase detected!

Billing process completed.
Month 1
Electricity Bill: Rs. 209.6

Month 2
Electricity Bill: Rs. 417.5

Month 3
Electricity Bill: Rs. 606.5

Month 4
Electricity Bill: Rs. 1032.5

===== MONTHLY BILL COMPARISON =====

Month 1 : Rs. 209.6

Month 2 : Rs. 417.5
Warning: Unusual increase detected!

Month 3 : Rs. 606.5
Bill is normal.

Month 4 : Rs. 1032.5
Warning: Unusual increase detected!

Billing process completed.

