class BankAccount:

    def __init__(self, account_number, account_holder, bank_name, branch,
                 balance, account_type, ifsc, mobile_number):

        self.account_number = account_number
        self.account_holder = account_holder
        self.bank_name = bank_name
        self.branch = branch
        self.balance = balance
        self.account_type = account_type
        self.ifsc = ifsc
        self.mobile_number = mobile_number

    def deposit(self):
        amount = int(input("Enter amount to deposit:"))
        self.balance = self.balance + amount 
        print("Amount Deposited Successfully")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw:"))
        self.balance = self.balance - amount
        print("Amount Withdrawn Successfully.")

    def check_balance(self):
        print("Current Balance:", self.balance)
 
    def transfer_money(self):
        amount = int(input("Enter amount to transfer: "))
        self.balance = self.balance - amount
        print("Money Transferred Successfully.")

    def print_statement(self):
        print("Account Details")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Bank Name:", self.bank_name)
        print("Branch:", self.branch)
        print("Balance:", self.balance)
        print("Account Type:", self.account_type)
        print("IFSC:", self.ifsc)
        print("Mobile Number:", self.mobile_number)

account1 = BankAccount(123456789,"Aryan","State Bank of India","Indore",50000,"Savings","SBIN0001234", "9876543210")

account1.print_statement()
account1.deposit()
account1.check_balance()
account1.withdraw()
account1.check_balance()
account1.transfer_money()
account1.check_balance()
    


    
    



