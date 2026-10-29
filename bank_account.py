import bank_account_functions
# welcome statement
print("Welcome to the Bank!")
user_name = input("Please enter your name: ")
user_account = bank_account_functions.BankAccount(user_name)
user_option = input("Please choose an option:\n1. Make a deposit\n2. Make a withdrawal\n3. View Account Information\n4. Quit\n")

while user_option != "4":
    if user_option == "1": # option one is deposit
        user_account.deposit()
    elif user_option == "2": # option two is withdrawal
        user_account.withdrawal()
    elif user_option == "3": #option three is to view account information
        user_account.view_account_info()
    else:  # if a customer enters an invalid menu choice, display an apporpriate message and allow them to try again.. continue displaying the menu until the customer chooses to quit.
        user_option = input("Invalid choice. Please try again. ")
        continue
    user_option = input("Please choose an option:\n1. Make a deposit\n2. Make a withdrawal\n3. View Account Information\n4. Quit\n")

user_account.quit() # OPTION 4 is to quit the program