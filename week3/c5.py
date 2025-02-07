class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds. Cannot withdraw more than the balance.")
        else:
            print("Withdrawal amount must be greater than zero.")

owner_name = input("Enter the account owner's name: ")
initial_balance = float(input("Enter the initial balance: "))

account1 = Account(owner_name, initial_balance)

while True:
    action = input("Would you like to deposit, withdraw or exit? (deposit/withdraw/exit): ").lower()
    
    if action == "deposit":
        deposit_amount = float(input("Enter deposit amount: "))
        account1.deposit(deposit_amount)
    elif action == "withdraw":
        withdraw_amount = float(input("Enter withdrawal amount: "))
        account1.withdraw(withdraw_amount)
    elif action == "exit":
        print(f"Final balance for {account1.owner}: {account1.balance}")
        break
    else:
        print("Invalid action. Please enter 'deposit', 'withdraw' or 'exit'.")