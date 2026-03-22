class Transaction:
    @staticmethod
    def transfer(amount, from_account, to_account):
        # Integration point: Uses withdraw and deposit which both trigger the logger
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False