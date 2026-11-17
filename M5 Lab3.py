import random
print("===== DICE SIMULATOR =====")
while True:
    choice = input("\nRoll the dice? (yes/no): ")
    if choice.lower() == "yes":
        number = random.randint(1, 6)
        print("Dice rolled:", number)
    elif choice.lower() == "no":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice! Enter yes or no.")
