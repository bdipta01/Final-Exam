import user

class Admin:
    def __init__(self) -> None:
        self.admin_list = {'ADMIN' : 'admin123'}

    def add_admin(self, user_name, password):
        if user_name in self.admin_list:
            print('Admin account is already created. Enter correct user_name and password')
        else:
            self.admin_list[user_name] = password

    def delete_account(self, acc_email):
        if acc_email in user.User.account_list:
            del user.User.account_list[acc_email]
        else:
            print('This account is not exist')

    def see_all_user_accounts(self):
        for user_details in user.User.account_list.values():
            print(f'Name : {user_details.name}, Email : {user_details.email}, Balance : {user_details.balance}, Account Number : {user_details.account_number}\n')

    def bank_available_balance(self):
        print(f'Bank available balance : {user.User.bank_fund}')

    def total_loan_amount(self):
        sum = 0
        for each_user in user.User.account_list.values():
            sum += each_user.loan_amount
        print(f'Total loan amount of all user : {sum}')

    def control_loan_feature(self, on_off):
        user.User.loan_feature = on_off



    


    
        

    