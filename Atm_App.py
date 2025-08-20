class Customer:
    def __init__(self, name, cid, accno, branch, bank):
        self.name = name
        self.cid = cid
        self.accno = accno
        self.branch = branch
        self.bank = bank
        self.balance = 0
        self.pin = 5566

    def display(self):
        print("\n--- Customer Details ---")
        print(f"Name: {self.name}")
        print(f"Customer ID: {self.cid}")
        print(f"Account No: {self.accno}")
        print(f"Branch: {self.branch}")
        print(f"Bank: {self.bank}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit Successful! New Balance: {self.balance}")
        else:
            print("Invalid Deposit Amount!")

    def withdraw(self, pin, amount):
        if pin != self.pin:
            print("Invalid PIN!")
        elif amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Withdraw Successful! Remaining Balance: {self.balance}")

    def check_balance(self, pin):
        if pin == self.pin:
            print(f"Available Balance: {self.balance}")
        else:
            print("Incorrect PIN!")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Incorrect old PIN!")


def atm_app():
    # Taking initial details
    name = input("Enter your name: ")
    branch = input("Enter branch: ")
    bank = input("Enter bank: ")
    cid = int(input("Enter cid: "))
    accno = int(input("Enter accno: "))

    customer = Customer(name, cid, accno, branch, bank)
    customer.display()

    while True:
        print("\n--- ATM Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Change PIN")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter deposit amount: "))
            customer.deposit(amount)

        elif choice == 2:
            pin = int(input("Enter PIN: "))
            amount = int(input("Enter withdraw amount: "))
            customer.withdraw(pin, amount)

        elif choice == 3:
            pin = int(input("Enter PIN: "))
            customer.check_balance(pin)

        elif choice == 4:
            old_pin = int(input("Enter old PIN: "))
            new_pin = int(input("Enter new PIN: "))
            customer.change_pin(old_pin, new_pin)

        elif choice == 5:
            print("Thank you! Visit again.")
            break

        else:
            print("Invalid choice!")
atm_app()
