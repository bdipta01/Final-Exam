import random

class User:
    bank_fund = 2000 #initially bank has this fund
    loan_feature = True
    account_list = {}

    def __init__(self, name, email, address, password, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transfer_history = [] #Here, save the deposit and withdraw history
        self.loans_taken = 0
        self.loan_amount = 0
        User.account_list[self.email] = self

    def generate_account_number(self):
        return random.randint(100000,999999)
    
    def deposit_amount(self, amount):
        self.balance += amount
        User.bank_fund += amount
        self.transfer_history.append(f'Deposit +{amount}, total amount : {self.balance}')
        print(f'{amount} is deposited')

    def withdraw_amount(self, amount):
        if amount > User.bank_fund:
            print('Bank is bankrupt')
        elif amount > self.balance:
            print('Withdrawal amount exceeded')
        else:
            self.balance -= amount
            User.bank_fund -= amount
            self.transfer_history.append(f'Withdraw -{amount}, total amount : {self.balance}')

    def available_balance(self):
        print(f'Available Balance of user {self.name}: {self.balance}')

    def transaction_history(self):
        if len(self.transfer_history) == 0:
            print('No transaction history')
        else:
            for transfer in self.transfer_history:
                print(f'Transaction History of user {self.name} : {transfer}\n')

    def loan_from_bank(self, amount):
        if User.loan_feature:
            self.loans_taken += 1
            if self.loans_taken <= 2:
                self.balance += amount 
                User.bank_fund -= amount
                self.loan_amount += amount
                self.transfer_history.append(f'Loan From Bank +{amount}, total amount : {self.balance}')
                print('Loan is approved')
            else:
                print('Loan is not approved as you already took loans two times')
        else:
            print('Loan Feature is Off')

    def transfer_amount(self, acc_email, amount): #other_account is a object of User Class
        if acc_email in User.account_list:
            other_account = User.account_list[acc_email]
            other_account.balance += amount
            self.balance -= amount
            self.transfer_history.append(f'Transfer -{amount}, total amount : {self.balance}')
            other_account.transfer_history.append(f'Received +{amount}, total amount : {other_account.balance}')
                
        else:
            print('Account does not exist')

    