import csv

while True:
    print("\n--- PAYROLL MANAGEMENT SYSTEM ---")
    print("1. Add Employee Payroll")
    print("2. View Payroll Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add employee payroll
    if choice == "1":
        emp_id = input("Enter Employee ID: ")

        while True:
            name = input("Enter Name: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("Invalid name! Please enter alphabets only (no numbers).")

        basic = float(input("Enter Basic Salary: "))

        hra = basic * 0.20
        da = basic * 0.10
        net_salary = basic + hra + da

        file = open("payroll.csv", "a", newline="")
        writer = csv.writer(file)
        writer.writerow([emp_id, name, basic, hra, da, net_salary])
        file.close()

        print("Payroll record added successfully.")

    # View payroll records
    elif choice == "2":
        print("\n--- PAYROLL REPORT ---")
        try:
            file = open("payroll.csv", "r")
            reader = csv.reader(file)
            for row in reader:
                print("ID:", row[0], "| Name:", row[1], "| Basic:", row[2], "| Net Salary:", row[5])
            file.close()
        except FileNotFoundError:
            print("No payroll records found.")

    # Exit
    elif choice == "3":
        print("Exiting Payroll System...")
        break

    else:
        print("Invalid choice.")