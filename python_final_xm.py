import random


class bank:

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.user_list = []
        self.admin_list = []
        self.loan = 0
        self.loan_status = False

    def create_user_account(self, customers):
        self.user_list.append(customers)
        print("Account created successfully!")

    def create_admin_account(self, ad):
        self.admin_list.append(ad)
        print("Admin account created Successfully")

    def check_available_balanced(self):
        print(f"balance is : {self.balance}")

    def remove_account(self, rem):
        var = self.find_user(rem)
        if var is not None:
            self.user_list.remove(var)
            print("Account remove successfully")
        else:
            print("Account not found")

    def find_user(self, email):
        for user in self.user_list:
            if user.email == email:
                return user
        return None

    def find_admin(self, email):
        for admin in self.admin_list:
            if admin.email == email:
                return admin
        return None

    def send_money(self, sender_email, rec_email, amount):
        send = self.find_user(sender_email)
        reciver = self.find_user(rec_email)
        if send is not None and reciver is not None:
            send.balance -= amount
            reciver.balance += amount
            print(f"Send from {sender_email} to {
                  rec_email} the amount is : {amount}successfully")

        else:
            print("User not found ")

    def show_user_list(self):
        print("**** User_list ****")
        for list in self.user_list:
            print(list.name)

    def set_loan_status(self):
        option = input(
            "Enter 'on' to enable or 'off' to disable loan status: ").lower()
        if option == 'on':
            self.loan_status = True
            print("Loan status enabled.")
        elif option == 'off':
            self.loan_status = False
            print("Loan status disabled.")
        else:
            print("Invalid option. Please enter 'on' or 'off'.")

    def total_loan_amount(self):
        total_loan = sum(customer.loan_taken for customer in self.user_list)
        print(f"Total loan amount: {total_loan}")


class user:
    def __init__(self, name,  email, address):
        self.name = name
        self.email = email
        self.address = address


class customer(user):
    max_loan = 2
    loan_taken = 0
    loan_status = True

    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.balance = 0
        self.accout_type = account_type
        self.transaction_history = []

    def check_available_balance(self):

        print(f"balance is : {self.balance}")

    def take_loan(self, amount):
        if self.loan_taken <= self.max_loan:
            if amount > 0:
                self.balance += amount
                self.loan_taken += 1
                print(f"Loan of {amount} granted successfully.")
            else:
                print("Invalid loan amount.")
        else:
            print("You have reached the maximum limit for taking loans (2 times max)")

    def deposit(self, amount, bank_ob):

        if (amount > 0):

            self.balance += amount
            bank_ob.balance += amount
            self.transaction_history.append(
                {"operation": "Deposite", "amount": amount, "balance": self.balance})
            print(f"Deposite {self.balance} successfully Done")

        else:
            print("Invalid deposite")

    def withdraw(self, amount, bank_ob):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                bank_ob.balance -= amount
                self.transaction_history.append(
                    {"operation": "withdraw", "amount": amount, "balance": self.balance})
                print(f"Withdrawn {amount} successfully.")
            else:
                print("Withdrawal amount exceeded.")
        else:
            print("Invalid withdrawal amount.")

    def tranfer_amount(self, rec_email1, amount, bank_obj1):
        bank_obj1.send_money(self.email, rec_email1, amount)
        self.transaction_history.append(
            {"operation": "send_money", "amount": amount, "balance": self.balance})

    def transaction_his(self):
        for info in self.transaction_history:
            print("operation\tamount\tbalance")
            print(f"{info["operation"]}\t {
                  info["amount"]} \t{info["balance"]}")


class admin(user, bank):

    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

    def create_admin(self, bank_ad):
        bank_ad.create_admin_account(self)

    def remove_user(self, bank_del):
        bank_del.remove_account()

    def view_user_list(self, bank_use):
        bank_use.show_user_list()

    def view_admin_list(self):
        pass

    def check_balance(self, bal):
        bal.check_available_balance()

    def check_loan(self, bank_ob):
        bank_ob.take_loan()

    def loan_status(self, bank_ob):
        bank_ob.set_loan_status()

    def check_balance(self):
        print(f"Balance of {self.name}: {self.balance}")


bank_ob = bank("islami")
first_admin = admin("Rahim", "rahim", "khulna")
first_admin.create_admin(bank_ob)


def customer_menu(customer_ob):
    while True:
        print("Customer Options:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Request Loan")
        print("5. Transaction History")
        print("6. Send Money")
        print("7. Exit")
        user_option = input("Enter your option: ")
        if user_option == "1":
            amount = float(input("Enter deposit amount: "))
            customer_ob.deposit(amount, bank_ob)
        elif user_option == "2":
            amount = float(input("Enter withdrawal amount: "))
            customer_ob.withdraw(amount, bank_ob)
        elif user_option == "3":
            customer_ob.check_available_balance()
        elif user_option == "4":
            amount = float(input("Enter loan amount: "))
            customer_ob.take_loan(amount)
        elif user_option == "5":
            customer_ob.transaction_his()
        elif user_option == "6":
            receiver_email = input("Enter receiver's email: ")
            amount = float(input("Enter transfer amount: "))
            customer_ob.tranfer_amount(receiver_email, amount, bank_ob)
        elif user_option == "7":
            print("exit done")
            break

        else:
            print("Invalid option. Please try again.")


def admin_menu():

    while True:
        print("******welcome to Admin Features *****")
        print("Admin Options:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Total Available Balance")
        print("5. Total loan amount")
        print("6. Loan Feature status")
        print("7. Exit")

        name = ""
        email = ""
        address = ""
        admin_ob = admin(name, email, address)
        option = int(input("Selecet your option : "))
        if option == 1:
            name = input("Enter name: ").lower()
            email = input("Enter email: ").lower()
            address = input("Enter address: ").lower()
            admin_ob = admin(name, email, address)
            admin_ob.create_admin(bank_ob)

        elif option == 2:
            account_number = input("Enter account number to delete: ")
            first_admin.remove_user(bank_ob, account_number)
        elif option == 3:
            first_admin.view_user_list(bank_ob)
        elif option == 4:
            bank_ob.check_available_balanced()
        elif option == 5:
            bank_ob.total_loan_amount()
        elif option == 6:
            first_admin.loan_status(bank_ob)
        elif option == 7:
            print("Exit")
            break
        else:
            print("Invalid option. Please try again.")


def admin_log_in():
    print("please  log in :")
    while True:
        email = input("Enter your email : ").lower()
        is_found = bank_ob.find_admin(email)

        if is_found is not None:
            admin_menu()
            return
        else:
            print("User not exceed")
            return


def user_auth():
    while True:
        print("1. Create account")
        print("2. Log in")
        print("3. Exit")
        print("Enter any option")
        authOption = int(input())

        if authOption == 1:
            print("create your account")
            print("Enter your name : ")
            name = input().lower()
            print("Enter your email : ")
            email = input().lower()
            print("Enter your address : ")
            address = input().lower()
            print("Enter your Account_type : ")
            accounttype = input().lower()

            if bank_ob.find_user(email) is not None:
                print("User Already Exist")
            else:
                crtAcc = customer(name, email, address, accounttype)

            bank_ob.create_user_account(crtAcc)
            customer_menu(crtAcc)
        elif authOption == 2:
            print("login for dashboard")
            email = input().lower()
            if bank_ob.find_user(email) is not None:
                customer_menu(bank_ob.find_user(email))
        elif authOption == 3:
            print("Exit Done")
            break

        else:
            print("user not found")


while True:
    print("Are you Admin or Customer?")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    option = int(input("Enter your option: "))

    if option == 1:
        user_auth()
    elif option == 2:
        admin_log_in()
    elif option == 3:
        print("Exit Done")
        break
    else:
        print("Invalid Input!!")
