# Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount. 
# A SavingsAccount object, in addition to the attributes of an Account object, 
# should have an interest attribute and a method which adds interest to the account. 
# A CurrentAccount object, in addition to the attributes of an Account object, should have an overdraft limit attribute.


# Now create a Bank class, an object of which contains an array of Account objects. 
# Accounts in the array could be instances of the Account class, the SavingsAccount class, or the CurrentAccount class. 
# Create some test accounts (some of each type).

# Write an update method in the Bank class. 
# It iterates through each account, updating it in the following ways: 
# Savings accounts get interest added (via the method you already wrote); 
# CurrentAccounts get a letter sent if they are in overdraft. (use print to 'send' the letter).

# The Bank class requires methods for opening and closing accounts, and for paying a dividend into each account.

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'
    

    
class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest
    def add_interest(self):
        self._balance += self._balance / 100 * self.interest

class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit
        self._balance += self.overdraft_limit

class Bank:
    def __init__(self):
        self._accounts = []
        
    def open_account(self, account):
        if account.get_balance() < 0:
            raise ValueError("Balance should be positive")
        self._accounts.append(account)


    def update(self):
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                if account._balance < account.overdraft_limit:
                    print(
                    f"You're in your overdraft limit. Your have {account._balance} quid left to reach the limit"
                    )



import unittest


class BankTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_open_account_with_positive_balance(self):
        account = Account.create_account('1')
        account.deposit(100)
        self.bank.open_account(account)
        self.assertIn(account, self.bank._accounts)

    def test_open_account_with_zero_balance(self):
        account = Account.create_account('2')
        self.bank.open_account(account)
        self.assertIn(account, self.bank._accounts)
        self.assertEqual(account.get_balance(), 0.0)

    def test_open_account_with_negative_balance(self):
        account = Account.create_account('3')
        account.withdraw(100) 
        with self.assertRaises(ValueError):
             self.bank.open_account(account)
        self.assertNotIn(account, self.bank._accounts)     

unittest.main()




