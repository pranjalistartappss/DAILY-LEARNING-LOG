class ATM:

    def __init__(self, account_number, card_number, pin, balance,
                 account_holder, bank_name, branch, atm_location):

        self.account_number = account_number
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
        self.account_holder = account_holder
        self.bank_name = bank_name
        self.branch = branch
        self.atm_location = atm_location

    def withdraw_cash(self):
        amount = int(input("Enter amount to withdraw: "))
        self.balance = self.balance - amount
        print("Cash Withdrawn Successfully.")

    def deposit_cash(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance = self.balance + amount
        print("Cash Deposited Successfully.")

    def check_balance(self):
        print("Current Balance:", self.balance)

    def change_pin(self):
        new_pin = input("Enter New PIN: ")
        self.pin = new_pin
        print("PIN Changed Successfully.")

    def mini_statement(self):
        print("Mini Statement")
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Bank Name:", self.bank_name)
        print("Branch:", self.branch)
        print("ATM Location:", self.atm_location)
        print("Current Balance:", self.balance)

atm1 = ATM(123456789,"9876543210123456","1234",50000,"Pranjali", "State Bank of India","Indore","Vijay Nagar")

atm1.mini_statement()
atm1.deposit_cash()
atm1.check_balance()
atm1.withdraw_cash()
atm1.check_balance()
atm1.change_pin()
atm1.mini_statement()