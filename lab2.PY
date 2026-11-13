students = {}

while True:
    print("\n--- STUDENT GRADING SYSTEM ---")
    print("1. Add Student Marks")
    print("2. View All Grades")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add student and calculate grade
    if choice == "1":
        while True:
            name = input("Enter student name: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("Invalid name! Please enter alphabets only (no numbers).")

        m1 = float(input("Enter marks for Subject 1: "))
        m2 = float(input("Enter marks for Subject 2: "))
        m3 = float(input("Enter marks for Subject 3: "))

        total = m1 + m2 + m3
        average = total / 3

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        students[name] = {
            "total": total,
            "average": round(average, 2),
            "grade": grade
        }

        print("Student record added successfully.")

    # View all student grades
    elif choice == "2":
        if len(students) == 0:
            print("No student records available.")
        else:
            print("\n--- GRADE REPORT ---")
            for name in students:
                print("Name:", name)
                print("Total:", students[name]["total"])
                print("Average:", students[name]["average"])
                print("Grade:", students[name]["grade"])
                print("-------------------")

    # Exit
    elif choice == "3":
        print("Exiting Student Grading System...")
        break

    else:
        print("Invalid choice.")