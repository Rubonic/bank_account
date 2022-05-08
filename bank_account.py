class BankAccount:

    all_accounts = []

    def __init__(self,int_rate,balance):
        self.balance = 0
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def print_all_balances(cls):
        for account in cls.all_accounts:
            print(f'Balance: ${account.balance}')

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficient funds: Chargin a $5 fee')
            self.balance - 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate*self.balance
        return self


John = BankAccount(0.02, 3000)
Terry = BankAccount(0.03, 10000)

John.deposit(500).deposit(1000).deposit(500).yield_interest().display_account_info()
Terry.deposit(600).deposit(300).withdraw(1000).withdraw(1000).withdraw(300).withdraw(1000).yield_interest().display_account_info()
        
BankAccount.print_all_balances()


    # def all_balances(cls):
    #     sum = 0
    #     # we use cls to refer to the class
    #     for account in cls.all_accounts:
    #         sum += account.balance
    #     return sum


