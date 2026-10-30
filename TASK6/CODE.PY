
n = int(input("Enter number of passengers: "))

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance in km: "))

    print("Classes: Sleeper / AC3 / AC2")
    travel_class = input("Enter travel class: ").upper()
    if age < 0 or distance <= 0:
        print("Invalid passenger details.")
        continue
    if distance <= 100:
        basic_fare = distance * 1

    elif distance <= 200:
        basic_fare = (100 * 1) + ((distance - 100) * 1.5)

    else:
        basic_fare = (100 * 1) + (100 * 1.5) + ((distance - 200) * 2)
    class_rates = {
        "SLEEPER": 1.0,
        "AC3": 1.5,
        "AC2": 2.0
    }

    if travel_class not in class_rates:
        print("Invalid travel class.")
        continue

    fare = basic_fare * class_rates[travel_class]
    concession = 0

    if age < 5:
        fare = 0

    elif age >= 60:
        concession = fare * 0.20
        fare = fare - concession
    reservation_fee = 40 if age >= 5 else 0

    total_fare = fare + reservation_fee

    cancel = input("Cancel ticket? (yes/no): ").lower()

    penalty = 0

    if cancel == "yes":
        penalty = total_fare * 0.20
        final_fare = penalty
        status = "Cancelled"

    elif cancel == "no":
        final_fare = total_fare
        status = "Confirmed"

    else:
        print("Invalid cancellation choice.")
        continue
    print("\n===== RAILWAY FARE DETAILS =====")
    print("Passenger Name:", name)
    print("Age:", age)
    print("Travel Distance:", distance, "km")
    print("Travel Class:", travel_class)
    print("Basic Fare: Rs.", round(basic_fare, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Cancellation Penalty: Rs.", round(penalty, 2))
    print("Final Amount: Rs.", round(final_fare, 2))
    print("Ticket Status:", status)

print("\nRailway booking process completed.")

