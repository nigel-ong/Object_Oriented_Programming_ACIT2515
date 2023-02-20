from customer import Customer


class Account:
    def __init__(self, owner:Customer, amount=0):
        """Creates a account object using owner from customer with amount the customer wants to add. Defaults to 0 if they have no money.

        Args:
            owner (Customer Object): A customer object that contains a name and a SSN
            amount (int, optional): A int amount of the amount of money the customer has. Defaults to 0.

        Raises:
            AttributeError: _description_
        """
        if not isinstance(owner,Customer):
            raise AttributeError("It is not the same type")
        self.owner = owner
        self.amount = amount 

    def deposit(self,money):
        """A method that allows a account to have money deposited

        Args:
            money (int or float): the amount of money to be deposited

        Raises:
            AttributeError: Must be a int or float
            AttributeError: Cannot be a negative amount of money
        """
        if type(money) not in (int,float):
            raise AttributeError("You can only add money.")
        if money < 1:
            raise AttributeError("You can only add a positive amount of money.")
        else:
            self.amount += money

    def withdraw(self,money):
        """A method that allows a account to have money withdrawn

        Args:
            money (int or float): the amount of money to be withdrawn

        Raises:
            AttributeError: Must be a int or float
            AttributeError: Cannot be a negative amount of money
        """
        if type(money) not in (int,float):
            raise AttributeError("Please enter an amount.")
        if money < 1:
            raise AttributeError("You can only add a positive amount of money.")
        else:
            self.amount -= money

    def transfer(self, account, amount):
        """Withdraws money from one account and deposits the same amount into another account.

        Args:
            account (Account Object): A account object instance
            amount (int or float): the amount from an Account object
        Raises:
            TypeError: The object must be a account object
        """
        if not isinstance(account,Account):
            raise TypeError("Make sure it is an account")
        else:
            self.withdraw(amount)
            account.deposit(amount)

class CreditAccount(Account):
    """Creates a Credit Account object with a additional method that calculates a new balance if the amount is negative with a admin fee

    Args:
        Account (Object): this is an account object being inherited from account
    """
    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest = interest_rate

    def compute_interest(self):
        admin_fee = 10
        if self.amount < 0:
            self.amount = self.amount * (100 + self.interest) / 100
            self.amount -= admin_fee

class SavingsAccount(Account):
    def __init__(self, owner):
        """Creates a savings account that is being inherited from the Account class, this amount cannot be below 0 

        Args:
            owner (Account Object): the argument is a object with 
        """
        super().__init__(owner)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise UserWarning("Savings account cannot be below 0")
        self._amount = value
