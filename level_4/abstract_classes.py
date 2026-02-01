from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,balance):
        self._balance = balance
        
    @property
    def balance(self):
        return self._balance
    
    def  deposit(self,amount):
        if amount > 0: 
            self._balance += amount
            print(f"An amount of {amount} has been deposited in your account successfully")
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def account_detail(self):
        pass
        
    

class SavingAccount(BankAccount):
    def __init__(self, balance, interest_rate, withdrawal_limit):
        self.balance = balance
        self.interest_rate = interest_rate
        self.withdrawal_limit = withdrawal_limit
        self.withdraws_done = 0
        
    def withdraw(self,amount):
        if self.withdraws_done < self.withdrawal_limit and amount <= self.balance:
            super().withdraw(amount)
            self.withdraws_done += 1
        else:
            print('Withdrawal limit exceeded')
    
    def account_detail(self):
        print(f"Account balance: {super().balance}")
        print(f"Interest rate: {self.interest_rate}")
        print(f"Withdrawals: {self.withdraws_done}/{self.withdrawal_limit}")
