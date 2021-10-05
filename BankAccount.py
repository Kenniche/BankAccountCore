class BankAccount:
    allBankAccounts = []


    def __init__(self, nameAccount, int_rate, balance): 
        self.nameAccount = nameAccount
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.allBankAccounts.append( self )
        print(f"{self.nameAccount}Initial Balance: ${self.balance}.") 
        

    def deposit( self, amount ):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print( "Insufficient funds: Charging a $5 fee." )
            self.balance -= 5
        return self

    def display_account_info( self ):
        print(f"{self.nameAccount}Account Balance: ${self.balance} | Interest rate: {self.int_rate} .")
        return self
        

    def yield_interest( self, int_rate ):
        if(self.balance > 0):
            self.balance += self.balance * int_rate
        return self  
    
    def printInfo(self):
        print(f"{self.nameAccount}Account Balance: ${self.balance}") 

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info  
    @classmethod
    def printAllAccountsInfo( cls ):
        print(f"Bank Account's Current Balance: ")
        for account in cls.allBankAccounts:
            account.printInfo()
        