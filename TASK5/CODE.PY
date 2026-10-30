data_usage = float(input("Enter required data (GB): "))
call_minutes = float(input("Enter required call minutes: "))
validity_required = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget: "))

n = int(input("\nEnter number of mobile plans: "))

eligible_plans = []

for i in range(n):

    print("\nEnter details of Plan", i + 1)

    name = input("Enter plan name: ")
    data_limit = float(input("Enter data limit (GB): "))
    call_limit = float(input("Enter call limit (minutes): "))
    validity = int(input("Enter validity (days): "))
    price = float(input("Enter plan price: "))
    data_rate = float(input("Enter excess data charge per GB: "))
    call_rate = float(input("Enter excess call charge per minute: "))
    excess_data = max(0, data_usage - data_limit)
    excess_calls = max(0, call_minutes - call_limit)
    extra_data_charge = excess_data * data_rate
    extra_call_charge = excess_calls * call_rate
   
  total_cost = price + extra_data_charge + extra_call_charge

    print("\nPlan:", name)
    print("Total Cost: Rs.", round(total_cost, 2))
   
    if validity >= validity_required and total_cost <= budget:

        eligible_plans.append({
            "name": name,
            "cost": total_cost,
            "validity": validity,
            "data": data_limit,
            "calls": call_limit
        })

        print("Status: Eligible")

    else:
        print("Status: Not Eligible")

print("\n===== PLAN COMPARISON =====")

if len(eligible_plans) == 0:

    print("No eligible mobile plans found.")

else:

    eligible_plans.sort(
        key=lambda x: (x["cost"], -x["validity"], x["name"].lower())
    )

    for i, plan in enumerate(eligible_plans, start=1):

        print("\nRank:", i)
        print("Plan Name:", plan["name"])
        print("Total Cost: Rs.", round(plan["cost"], 2))
        print("Validity:", plan["validity"], "days")

    best_plan = eligible_plans[0]

    print("\n===== BEST MOBILE PLAN =====")
    print("Plan Name:", best_plan["name"])
    print("Minimum Cost: Rs.", round(best_plan["cost"], 2))
    print("Validity:", best_plan["validity"], "days")

print("\nPlan optimization completed.")

