name = input("Enter patient name: ")

category = input(
    "Enter patient category (Normal/Senior/Student): "
).lower()
consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")

else:
   
    total_bill = consultation + diagnostic + treatment
    concession = 0

    if category == "senior":
        concession = total_bill * 0.20

    elif category == "student":
        concession = total_bill * 0.10

    elif category == "normal":
        concession = 0

    else:
        print("Invalid patient category!")
        exit()

    
    final_bill = total_bill - concession

    print("\n===== HOSPITAL BILL =====")
    print("Patient Name:", name)
    print("Total Bill: Rs.", round(total_bill, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Final Bill: Rs.", round(final_bill, 2))

    
    paid = float(input("\nEnter amount paid: "))

   
    if paid < 0 or paid > final_bill:
        print("Invalid payment amount!")

    else:
        if paid == final_bill:
            status = "Fully Paid"

        elif paid > 0:
            status = "Partially Paid"

        else:
            status = "Unpaid"

        balance = final_bill - paid

       
        print("\n===== PAYMENT DETAILS =====")
        print("Amount Paid: Rs.", round(paid, 2))
        print("Remaining Balance: Rs.", round(balance, 2))
        print("Patient Classification:", status)

        print("\nBilling process completed.")

