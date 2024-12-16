from prettytable import PrettyTable

class BankAccount:
    accounts = {}

    def __init__(self, account_number):
        self.balance = 0
        self.account_number = account_number
        self.transactions = []
        BankAccount.accounts[account_number] = self

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            print(f"Withdrew {amount}. New Balance: {self.balance}")
            return amount
        else:
            print("Insufficient balance.")
            return 0

    def transform(self, target_account, amount):
        if target_account in BankAccount.accounts:
            target = BankAccount.accounts[target_account]
            withdrawn_amount = self.withdraw(amount)
            if withdrawn_amount > 0:
                target.deposit(withdrawn_amount)
                self.transactions.append(f"Transferred {withdrawn_amount} to {target_account}")
                print(f"Transferred {withdrawn_amount} to account {target_account}.")
        else:
            print("Target account number not found.")

    def __str__(self):
        table = PrettyTable()
        table.field_names = ["Account Number", "Balance"]
        table.add_row([self.account_number, self.balance])
        table.add_row(["Transactions", "\n".join(self.transactions)])  # إضافة سجل العمليات
        return table.get_string()

# Testing
account1 = BankAccount(123)
account1.deposit(1000)
account2 = BankAccount(1)
account1.transform(1, 600)
print(account1)



