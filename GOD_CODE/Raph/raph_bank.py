class Customer:
    """
    A simple class that represents a customer at the bank.
    """

    def __init__(self, name, ssn):
        if type(name) is not str or len(name) < 2:
            raise AttributeError("Invalid name for the account.")
        
        if type(ssn) is not str or not ssn.isnumeric():
            raise AttributeError("Invalid SSN for the account.")

        self.name = name
        self.ssn = ssn


from account import Account, CreditAccount, SavingsAccount

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, category, owner, interest_rate=0):
        if category == "credit":
            account = CreditAccount(owner, interest_rate)
        elif category == "savings":
            account = SavingsAccount(owner, interest_rate)
        else:
            account = Account(owner)
        self.accounts.append(account)
        return account

    def find_accounts_by_ssn(self, ssn):
        return [account for account in self.accounts if account.owner.ssn == ssn]

    def find_accounts_by_name(self, name):
        return [account for account in self.accounts if name.lower() in account.owner.name.lower()]

    @property
    def balance(self):
        return sum(account.amount for account in self.accounts)
    

from customer import Customer

class Account:
    def __init__(self, owner, amount=0):
        if not isinstance(owner, Customer):
            raise AttributeError(f"Invalid owner for the account, expected a Customer instance but got {(type(owner))}")
        self.owner = owner
        self.amount = amount

    def deposit(self, amount):
        if amount < 0:
            raise AttributeError("Invalid deposit amount.")
        self.amount += amount

    def withdraw(self, amount):
        if amount < 0:
            raise AttributeError("Invalid withdraw amount.")
        self.amount -= amount

    def transfer(self, account, amount):
        if not isinstance(account, Account):
            raise TypeError("Invalid account type.")
        self.withdraw(amount)
        account.deposit(amount)

class CreditAccount(Account):
    def __init__(self, owner, interest, amount=0):
        super().__init__(owner, amount)
        self.interest = interest

    def compute_interest(self):
        if self.amount < 0:
            self.amount = self.amount * (100 + self.interest) / 100
            self.amount -= 10

class SavingsAccount(Account):
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if value < 0:
            raise UserWarning("Invalid amount for savings account.")
        self._amount = value