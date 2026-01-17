class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    
    @property 
    def balance(self):
        print(self.__balance)
    
    
    def deposit(self,amount):
        if amount >= 0:
            self.__balance =  self.__balance + amount
            return self.__balance
        else:
            print("Please check the number u entered")
    
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance =  self.__balance - amount
            return self.__balance
        else:
            print("Insufficient funds")


account_1 = BankAccount(1000)
account_1.balance

account_1.withdraw(200)
account_1.balance

account_1.deposit(500)
account_1.balance