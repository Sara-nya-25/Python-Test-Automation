
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def apply_interest(self, rate_percentage):
        self.balance += self.balance * (rate_percentage / 100)

class BankSystem:
    @staticmethod
    def transfer(from_account, to_account, amount):
        from_account.withdraw(amount)
        to_account.deposit(amount)