from account import Account 

class SavingsAccount(Account):
    def __init__(self, owner):
        super().__init__(owner)

    @property
    def amount(self):
        if self.amount < 0:
            self.amount = 0
        return self.amount






