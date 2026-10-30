

eligible_students = []
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

n = int(input("Enter number of students: "))

for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    aggregate = float(input("Enter aggregate marks: "))

    subjects = int(input("Enter number of subjects: "))

    subject_marks = []

    for j in range(subjects):
        mark = float(input(f"Enter marks in subject {j+1}: "))
        subject_marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))

    income = float(input("Enter annual family income: "))

    # Checking Eligibility
    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARKS for mark in subject_marks) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        print(name, "is Eligible for Scholarship")

        eligible_students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

    else:
        print(name, "is Not Eligible for Scholarship")


# Ranking Eligible Students
eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"],
        x["name"].lower()
    
print("\n===== SCHOLARSHIP ALLOCATION RESULTS =====")

if len(eligible_students) == 0:
    print("No students are eligible for scholarship.")

else:
    print("\nRank  Name       Aggregate  Attendance  Income")

    for rank, student in enumerate(eligible_students, start=1):

        print(
            rank,
            student["name"],
            student["aggregate"],
            student["attendance"],
            student["income"]
        )

print("\nScholarship allocation process completed.")

