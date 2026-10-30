name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

if min(basic, allowances, overtime_hours,
       overtime_rate, incentives) < 0:

    print("Invalid input! Values cannot be negative.")

else:
    overtime_pay = overtime_hours * overtime_rate
    gross_salary = basic + allowances + overtime_pay + incentives
    if gross_salary <= 10000:
        deduction = gross_salary * 0.05

    elif gross_salary <= 20000:
        deduction = (10000 * 0.05) + ((gross_salary - 10000) * 0.10)

    else:
        deduction = (10000 * 0.05) + (10000 * 0.10) + ((gross_salary - 20000) * 0.15)

    net_salary = gross_salary - deduction

    print("\n========== SALARY STATEMENT ==========")
    print("Employee Name       :", name)
    print("Basic Salary        : Rs.", basic)
    print("Allowances          : Rs.", allowances)
    print("Overtime Pay        : Rs.", overtime_pay)
    print("Incentives          : Rs.", incentives)
    print("--------------------------------------")
    print("Gross Salary        : Rs.", round(gross_salary, 2))
    print("Total Deductions    : Rs.", round(deduction, 2))
    print("--------------------------------------")
    print("Net Salary          : Rs.", round(net_salary, 2))
    print("======================================")

