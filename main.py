from user import User
from admin import Admin

class Mainn:
    def __init__(self) -> None:
        self.user = None

    def main_menu(self):
        while True:
            print('***********Welcome to OUR Bank***********')
            print('Select User or Admin\nCreate Account, press 1\nFor Admin, press 2\nFor user login, press 3\nPress 4 for Exit')
            select = int(input())
            if select == 1:
                print('Thank you for choosing us. For new account, we need your name, email, address, password, account_type')
                name = input('Your Name : ')
                email = input('Your Email : ')
                address = input('Yout Address : ')
                password = input('Your Password : ')
                account_type = input('Account Type : ')
                user_user = User(name, email, address, password, account_type)
                print(f'Thank you {name} for creating a account yourself')

            elif select == 2:
                print('Welcome to Admin Login')
                admin_user_name = input('Enter Admin User Name : ')
                admin_pass = input('Enter Admin Password : ')
                admin = Admin()
                if admin_user_name in admin.admin_list:
                    if admin.admin_list[admin_user_name] == admin_pass:
                        self.admin_display()
                    else:
                        print('Wrong Admin User Name and Password')
                else:
                    print('Enter correct user_name and password')


            elif select == 3:
                print('Welcome to User Login')
                email = input('Enter your email : ')
                password = input('Enter your password : ')
                if email in User.account_list:
                    User.account_list[email].password == password
                    self.user = User.account_list[email]
                    self.user_display()
                else:
                    print('There is no account, you have to create first')
            
            
            elif select == 4:
                break

    def admin_display(self):
        while True:
            print('Option 1 : Create Account')
            print('Option 2 : Delete Account')
            print('Option 3 : See ALL Account')
            print('Option 4 : See Bank Total Available Balance')
            print('Option 5 : See Total Loan Amount')
            print('Option 6 : On and Off of bank\'s Loan Feature')
            print('Option 7 : On and Off of bank\'s Loan Feature')
            print('Option 8 : Exit')

            admin = Admin()
            option = int(input())

            if option == 1:
                print('Thank you for choosing us. For new account, we need your name, email, address, password, account_type')
                name = input('Your Name : ')
                email = input('Your Email : ')
                address = input('Yout Address : ')
                password = input('Your Password : ')
                account_type = input('Account Type : ')
                user_user = User(name, email, address, password, account_type)
                print(f'Thank you {name} for creating a account')

            elif option == 2:
                print('Choose which account, you want to delete. Enter the account email')
                acc_email = input('Enter Email : ')
                admin.delete_account(acc_email)

            elif option == 3:
                print('All User of Bank')
                admin.see_all_user_accounts()

            elif option == 4:
                admin.bank_available_balance()

            elif option == 5:
                admin.total_loan_amount()

            elif option == 6:
                feature = input('Normally feature is ON. For Off, press 0, For on, press 1')
                admin.control_loan_feature(feature)

            elif option == 7:
                user_name = input('Enter Admin user_name : ')
                password = input('Enter login password : ')
                admin = Admin()
                admin.add_admin(user_name, password)

            elif option == 8:
                break
                    
    def user_display(self):
        while True:
            print('Option 1 : Create Account by User')
            print('Option 2 : Deposit Amount')
            print('Option 3 : Withdraw Amount')
            print('Option 4 : Check Balance')
            print('Option 5 : Check Transaction History')
            print('Option 6 : Taken Loan')
            print('Option 7 : Transfer Amount')
            print('Option 8 : Log out')

            option = int(input())

            if option == 1:
                print('Thank you for choosing us. For new account, we need your name, email, address, account_type')
                name = input('Your Name : ')
                email = input('Your Email : ')
                address = input('Yout Address : ')
                account_type = input('Account Type : ')
                user_user = User(name, email, address, account_type)
                print('Thank you for creating a account yourself')

            elif option == 2:
                amount = int(input('Enter Your Deposit Amount : '))
                self.user.deposit_amount(amount)
            
            elif option == 3:
                amount = int(input('Enter Your Withdrawal Amount : '))
                self.user.withdraw_amount(amount)

            elif option == 4:
                self.user.available_balance()

            elif option == 5:
                self.user.transaction_history()

            elif option == 6:
                amount = int(input('Enter Your Loan Amount : '))
                self.user.loan_from_bank(amount)

            elif option == 7:
                amount = int(input('Enter Your Transfer Amount : '))
                acc_email = input('Enter Acount Email, where you want to transfer. Please enclosed email with\'\'')
                self.user.transfer_amount(acc_email, amount)

            elif option == 8:
                break

if __name__ == "__main__":
    main = Mainn()
    main.main_menu()