# Area Calculator

import math

print("===== AREA CALCULATOR =====")

print("\n1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Triangle")
print("4. Area of Square")

choice = int(input("Enter your choice: "))

if choice == 1:
    radius = float(input("Enter radius: "))

    area = math.pi * radius * radius

    print("Area of Circle:", area)

elif choice == 2:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    area = length * breadth

    print("Area of Rectangle:", area)

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    area = 0.5 * base * height

    print("Area of Triangle:", area)

elif choice == 4:
    side = float(input("Enter side: "))

    area = side * side

    print("Area of Square:", area)

else:
    print("Invalid choice.")