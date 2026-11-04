class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self._account_number = account_number
        self._balance = balance
        self._owner_name = owner_name
    
    # Getter methods
    def get_account_number(self):
        return self._account_number
    
    def get_balance(self):
        return self._balance
    
    def get_owner_name(self):
        return self._owner_name
    
    # Setter methods
    def set_account_number(self, account_number):
        self._account_number = account_number
    
    def set_owner_name(self, owner_name):
        self._owner_name = owner_name

    # Method to deposit and withdraw

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False
 # Method to display the Account into
    def display_info(self):
        print(f"Account Number: {self._account_number}")
        print(f"Owner: {self._owner_name}")
        print(f"Balance: ${self._balance:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, owner_name, interest_rate):
       super().__init__(account_number, balance, owner_name)
       self.interest_rate = interest_rate
    def describe_account(self):
        super().display_info()
        return f"rate: {self.interest_rate}"
    

# account = BankAccount("1234567", 1000.0, "John Doe")
# account.display_info()
# account.deposit(account.get_balance()+500)
# account.withdraw(200)
# print("--------------------------")
# account.display_info()

mysavings = SavingsAccount("1234567", 1000.0, "John Doe", 0.2)
print(mysavings.describe_account())