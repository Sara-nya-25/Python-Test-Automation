class BankAccount:
    def __init__(self, owner, balance, logger):
        self.owner = owner
        self.balance = balance
        self.logger = logger

    def deposit(self, amount):
        self.balance += amount
        self.logger.log(f"deposit: {amount} kr, balance {self.balance} kr")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.logger.log(f"withdraw: {amount} kr, balance {self.balance} kr")
            return True
        else:
            self.logger.log(f"withdraw: could not withdraw {amount} kr from account")
            return False