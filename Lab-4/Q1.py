# Lab 4 - Unit Converter

print("===== UNIT CONVERTER =====")

print("\n1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Kilograms to Pounds")
print("6. Pounds to Kilograms")

choice = int(input("\nEnter your choice: "))
value = float(input("Enter value: "))

if choice == 1:
    result = value * 0.621371
    print("Miles:", result)

elif choice == 2:
    result = value * 1.60934
    print("Kilometers:", result)

elif choice == 3:
    result = (value * 9 / 5) + 32
    print("Fahrenheit:", result)

elif choice == 4:
    result = (value - 32) * 5 / 9
    print("Celsius:", result)

elif choice == 5:
    result = value * 2.20462
    print("Pounds:", result)

elif choice == 6:
    result = value * 0.453592
    print("Kilograms:", result)

else:
    print("Invalid choice.")