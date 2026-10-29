# when customer chooses to view account information, display, the customer's name, account number, and current
# your program shiuld use a bankaccount class to represent the customer's account. organize your program into at least two python files so that the class and the program are separate
import random #to assign a random account number to the customer

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(10000, 99999)
        self.account_balance = 0.00

    # when customer makes a deposit, ask how much money they would like to add to the account
    def deposit(self):
        deposit_amount = float(input("How much would you like to deposit? "))
        while deposit_amount <= 0: # no negative deposits
            print("Please enter a positive amount. ")
            deposit_amount = float(input("How much would you like to deposit? "))
        self.account_balance += deposit_amount

    # when customers makes a withdrawal, ask how much money they would like to withdraw.
    # program should not allow customer to withdraw more money than they currently have in the account. 
    def withdrawal(self):
        if self.account_balance == 0:
            print("You do not have enough funds to make a withdrawal. ")
            return # end the method
        withdrawal_amount = float(input("How much would you like to withdraw? "))
        while withdrawal_amount > self.account_balance or withdrawal_amount <= 0: # no negative withdrawals or withdrawals greater than the account balance
            print("You do not have enough funds to make this withdrawal. ")
            withdrawal_amount = float(input("How much would you like to withdraw? "))
        self.account_balance -= withdrawal_amount

    def view_account_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Account Number: #{self.account_number}")
        print(f"Balance: ${self.account_balance:.2f}")

    def quit(self):
        print("Thank you for your business!")