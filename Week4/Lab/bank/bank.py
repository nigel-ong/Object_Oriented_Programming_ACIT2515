from account import Account, CreditAccount, SavingsAccount
from customer import Customer


class Bank:
    def __init__(self, name:str) -> None:
        """Creates a Bank object

        Args:
            name (str): Name of the bank object you want create.    
        """
        self.name = name
        self.listacct = []
        
    
    def create_account(self, category:str, owner:Customer, interest_rate:int=0):
        """

        Args:
            category (str): 1 of 3 account types. 
            owner (Customer): The customer object from customer.
            interest_rate (int, optional): An optional interest rate that is only applied with a credit account. Defaults to 0.

        Raises:
            AttributeError: If the string entered into category is not one of the 3 types

        Returns:
            _type_: returns the list of accounts associated with a customer 
        """
        acttype = ["account", "credit", "savings"]
        if category.lower() in acttype:
            if category.lower() == "account":
                acct = Account(owner)
            elif category.lower() == "savings":
                acct = SavingsAccount(owner)
            elif category.lower() == "credit":
                acct = CreditAccount(owner, interest_rate)
        else:
            raise AttributeError("Please enter account, credit, or savings")
        self.listacct.append(acct)
        return acct
        

    def find_accounts_by_ssn(self,ssnum:str):
        """Receives a string that will be used to compare and check if any accounts have that string as its ssn from Customer class

        Args:
            ssnum (str): A string that you enter you are trying to match to a ssn

        Returns:
            (list): returns a list of the accounts that match the ssn 
        """
        ssnlist = []
        for acct in self.listacct:
            if ssnum == acct.owner.ssn:
                ssnlist.append(acct)
        return ssnlist

    def find_accounts_by_name(self,name):
        """Receives a string that will be used to compare and check if any accounts have that string as its name from Customer class

        Args:
            name (str): A string that you enter you are trying to match to a name 

        Returns:
            (list): returns a list of the accounts that match the name
        """
        namelist = []
        for acct in self.listacct:
            if name == acct.owner.name:
                namelist.append(acct)
        return namelist

    
    @property
    def balance(self):
        """The balance of all amounts of all bank accounts managed by a bank

        Returns:
            (int): returns the sum of all accounts managed by the bank
        """
        total_balance = 0
        for acc in self.listacct:
            total_balance += acc.amount
        return total_balance
    
