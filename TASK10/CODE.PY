total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
threshold = float(input("Enter required attendance percentage: "))

if (total_classes < 0 or attended_classes < 0 or
    attended_classes > total_classes or
    threshold <= 0 or threshold > 100):

    print("Invalid attendance details.")

else:
    current_percentage = (
        attended_classes / total_classes * 100
        if total_classes > 0 else 0
    )

    print("\n===== ATTENDANCE REPORT =====")
    print("Total Classes:", total_classes)
    print("Classes Attended:", attended_classes)
    print("Current Attendance:", round(current_percentage, 2), "%")

    if current_percentage >= threshold:
        print("Eligibility Status: Eligible")
        print("Additional Classes Required: 0")

    elif threshold == 100:
        print("Eligibility Status: Not yet eligible")
        print("All future classes must be attended.")

    else:
        required_classes = 0

        while (
            (attended_classes + required_classes) /
            (total_classes + required_classes) * 100
        ) < threshold:
            required_classes += 1

        print("Eligibility Status: Not yet eligible")
        print("Minimum Consecutive Classes Required:",
              required_classes)
    future_classes = int(input("\nEnter upcoming number of classes: "))

    if future_classes < 0:
        print("Invalid number of future classes.")

    else:
        scenarios = [100, 80, 50]

        print("\n===== FUTURE ATTENDANCE SCENARIOS =====")

        for rate in scenarios:
            future_attended = int(future_classes * rate / 100)

            future_percentage = (
                (attended_classes + future_attended) /
                (total_classes + future_classes) * 100
                if total_classes + future_classes > 0 else 0
            )

            print("\nFuture Attendance:", rate, "%")
            print("Classes Attended:", future_attended)
            print("Projected Attendance:",
                  round(future_percentage, 2), "%")

            if future_percentage >= threshold:
                print("Status: Eligible")
            else:
                print("Status: Not Eligible")

    print("\nAttendance analysis completed.")

