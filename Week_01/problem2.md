Problem 2 (Medium): Bank Account Management
Create a BankAccount class that manages individual accounts while tracking bank-wide statistics.

Requirements:

1. Define a class BankAccount with these class variables:
bank_name = “Urgench Bank”
total_accounts = 0 (tracks how many accounts have been created)
min_balance = 10 (minimum balance requirement)
2. Define __init__ with parameters owner and initial_balance:
Store as instance variables: self.owner and self.balance
Increment the class variable BankAccount.total_accounts by 1 each time an account is created
3. Create a method deposit(self, amount):
Add the amount to the balance
Print: "Deposited {amount}. New balance: {new_balance}"
Only process if amount > 0
4. Create a method withdraw(self, amount):
Check if withdrawal would leave balance below BankAccount.min_balance
If sufficient funds: subtract amount and print "Withdrew {amount}. New balance: {new_balance}"
If insufficient: print "Insufficient funds or below minimum balance"
5. Create a method display_account_info(self) that prints: "Owner: {owner}, Balance: {balance}, Bank: {bank_name}"

6. Create two accounts and demonstrate all functionality:
Account 1: “Ali”, 100
Account 2: “Vali”, 50
Display Ali’s account info
Deposit 50 to Ali’s account
Withdraw 80 from Ali’s account (should work)
Display Vali’s account info
Withdraw 100 from Vali’s account (should fail - below minimum)
Print total accounts count

Expected Output
```
Owner: Ali, Balance: 100, Bank: Urgench Bank
Deposited 50. New balance: 150
Withdrew 80. New balance: 70
Owner: Vali, Balance: 50, Bank: Urgench Bank
Insufficient funds or below minimum balance
Total accounts created: 2
```