# Simple Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Addition:", a + b)

elif choice == 2:
    print("Subtraction:", a - b)

elif choice == 3:
    print("Multiplication:", a * b)

elif choice == 4:
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid choice.")