class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            
    def withdraw(self,amount):
        if amount <= self.__balance :
            self.__balance -= amount
    
    def account_detail(self):
        print(f"Account balance is {self.__balance}")
        
        
        
class SavingAccount(BankAccount):
    def __init__(self, balance, interest_rate, withdrawal_limit):
        super().__init__(balance)
        self.interest_rate = interest_rate
        self.withdrawal_limit = withdrawal_limit
        self.withdraws_done = 0
        
    def withdraw(self,amount):
        if self.withdraws_done < self.withdrawal_limit:
            super().withdraw(amount)
            self.withdraws_done += 1
        else:
            print('Withdrawal limit exceeded')
    
    def account_detail(self):
        print(f"Account balance: {super().balance}")
        print(f"Interest rate: {self.interest_rate}")
        print(f"Withdrawals: {self.withdrawal_limit}")
        

my_savings = SavingAccount(balance=1000, interest_rate=0.05, withdrawal_limit=3)
my_savings.withdraw(400)
my_savings.account_detail()

my_savings.withdraw(400)

my_savings.account_detail()

my_savings.withdraw(10000)
