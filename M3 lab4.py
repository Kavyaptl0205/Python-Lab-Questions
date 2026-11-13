attendance = {}

while True:
    print("\n--- ATTENDANCE TRACKER ---")
    print("1. Mark Attendance")
    print("2. View Attendance Report")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Mark attendance
    if choice == "1":
        while True:
            name = input("Enter student name: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("Invalid name! Please enter alphabets only (no numbers).")

        status = input("Enter status (P for Present / A for Absent): ").upper()

        if name not in attendance:
            attendance[name] = {"present": 0, "total": 0}

        attendance[name]["total"] = attendance[name]["total"] + 1

        if status == "P":
            attendance[name]["present"] = attendance[name]["present"] + 1

        print("Attendance marked successfully.")

    # View report
    elif choice == "2":
        if len(attendance) == 0:
            print("No attendance records found.")
        else:
            print("\n--- ATTENDANCE REPORT ---")
            for name in attendance:
                present = attendance[name]["present"]
                total = attendance[name]["total"]
                percentage = (present / total) * 100

                print("Student:", name)
                print("Present:", present, "/", total)
                print("Percentage:", round(percentage, 2), "%")
                print("-------------------")

    # Exit
    elif choice == "3":
        print("Exiting Attendance Tracker...")
        break

    else:
        print("Invalid choice.")