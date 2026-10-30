product_name = input("Enter product name: ")

quantity = int(input("Enter production quantity: "))
material_cost = float(input("Enter material cost per unit: "))
labour_cost = float(input("Enter labour cost per unit: "))
wastage_percentage = float(input("Enter wastage percentage: "))
machine_cost = float(input("Enter machine cost per unit: "))
selling_price = float(input("Enter selling price per unit: "))

profit_target = float(input("Enter target profit percentage: "))

if (quantity <= 0 or
    min(material_cost, labour_cost, wastage_percentage,
        machine_cost, selling_price, profit_target) < 0):

    print("Invalid input! Please enter valid positive values.")

elif wastage_percentage > 100:

    print("Wastage percentage cannot exceed 100.")

else:
    total_material = material_cost * quantity

    total_labour = labour_cost * quantity

    wastage_cost = total_material * wastage_percentage / 100

    total_machine = machine_cost * quantity

    total_cost = (
        total_material +
        total_labour +
        wastage_cost +
        total_machine
    )

    total_revenue = selling_price * quantity
    profit = total_revenue - total_cost
    profit_percentage = (profit / total_cost * 100
                         if total_cost > 0 else 0)

  
    if profit_percentage >= profit_target:
        status = "Profit Target Achieved"
    else:
        status = "Profit Target Not Achieved"

   
    print("\n===== MANUFACTURING REPORT =====")

    print("Product Name       :", product_name)
    print("Production Quantity:", quantity)

    print("\n----- COST DETAILS -----")
    print("Material Cost      : Rs.", round(total_material, 2))
    print("Labour Cost        : Rs.", round(total_labour, 2))
    print("Wastage Cost       : Rs.", round(wastage_cost, 2))
    print("Machine Cost       : Rs.", round(total_machine, 2))

    print("\nTotal Cost         : Rs.", round(total_cost, 2))
    print("Total Revenue      : Rs.", round(total_revenue, 2))
    print("Total Profit       : Rs.", round(profit, 2))
    print("Profit Percentage  :", round(profit_percentage, 2), "%")

    print("\nProfitability Status:", status)

    print("\nManufacturing analysis completed.")

