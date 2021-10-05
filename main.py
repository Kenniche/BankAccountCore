from BankAccount import BankAccount

# Create 2 accounts	
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

PrimaryBankAccount = BankAccount( "Salary ", 0.02, 250 )
SecondaryBankAccount = BankAccount( "Savings ", 0.03, 3000 )


PrimaryBankAccount.deposit(500).deposit(500).deposit(500).withdraw(200).yield_interest( 0.02 ).display_account_info()
SecondaryBankAccount.deposit(500).deposit(500).withdraw(150).withdraw(150).withdraw(150).withdraw(100).yield_interest( 0.03 ).display_account_info()


# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

BankAccount.printAllAccountsInfo()






