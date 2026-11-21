def add():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")

    with open("students.txt", "a") as file:
        file.write(roll + "," + name + "," + marks + "\n")

    print("Student record added successfully!")


def display():
    try:
        with open("students.txt", "r") as file:
            print("\n--- Student Records ---")

            for line in file:
                roll, name, marks = line.strip().split(",")

                print("Roll Number:", roll)
                print("Student Name:", name)
                print("Marks:", marks)
                print("-------------------")

    except FileNotFoundError:
        print("No student records found.")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add()

    elif choice == "2":
        display()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")