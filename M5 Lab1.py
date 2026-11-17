class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs. {amount:.2f} deposited successfully!")
        else:
            print("Please enter a valid deposit amount.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Rs. {amount:.2f} withdrawn successfully!")
    def check_balance(self):
        print(f"Current Balance: Rs. {self.balance:.2f}")
    def display_details(self):
        print("\n----- Account Details -----")
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print(f"Balance: Rs. {self.balance:.2f}")
print("===== BANK ACCOUNT SYSTEM =====")
name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
account = BankAccount(name, account_number)
while True:
    print("\n----- MENU -----")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")
    choice = input("Enter your choice: ")
    try:
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.display_details()
        elif choice == "5":
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice! Please select 1 to 5.")
    except ValueError:
        print("Invalid input! Please enter a numeric amount.")