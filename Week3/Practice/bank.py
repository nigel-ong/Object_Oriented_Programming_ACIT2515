class BankAccount:
    def __init__(self):
        self.amount = 0

    def deposit(self, value):
        self._amount += value
    
    def withdraw(self,value):
        self._amount -= value


    @property
    def amount(self):
        return self._amount 

    @amount.setter
    def amount(self,value):
        if value < 0:
            print("no you're poor")
            return
        self._amount = value