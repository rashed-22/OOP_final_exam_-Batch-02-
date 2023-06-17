class Person:
    def __init__(self, email, password, acc_no) -> None:
        self.email = email
        self.password = password
        self.acc_no = acc_no

class Bank:
    account_list = []
    bank_balance = 50000
    total_loan_amount = 0
    

    def account_details(self):
        print()
        print(f"{' '*10} Account Details {' '*10}")
        for user in self.account_list:
            print(f"email: {user['email']} password: {user['password']} account no: {user['acc_no']}")

    def get_user(self):
        return self.account_list

   

   

class User(Bank):
    balance = 0
    acc_no = 0
    transactions = []
    def create_account(self):
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        acc_no = int(input('Enter your account no: '))
        new_user = Person(email, password, acc_no)
        self.account_list.append(vars(new_user))
        print('Account Created Successfully...!')



    def deposit(self):
        amount = int(input('Enter your deposit_amount: '))
        account_no = int(input('Enter your account no to deposit: '))
        for acc in self.account_list:
            if account_no == acc['acc_no']:
                if amount > 500:
                    self.balance += amount
                    self.bank_balance += amount
                    print(f"Successfully Deposited: {amount}")
                    self.transactions.append(f"credit: +{amount}")
                else:
                    print('You have to deposit more than 500')
        
    def withdraw(self):
        amount = int(input('Enter your withdraw_amount: '))
        account_no = int(input('Enter your account no to withdraw: '))
        for acc in self.account_list:
            if account_no == acc['acc_no']:
                if amount <= self.balance:
                    self.balance -= amount
                    self.bank_balance -= amount
                    print(f"Succssfully Withdraw: {amount}")
                    self.transactions.append(f"debit: -{amount}")
                else:
                    print('The bank is bankrupt...!')
            
    
    def check_available_balance(self):
        account_no = int(input('Enter your account no to check balance: '))
        for acc in self.account_list:
            if account_no == acc['acc_no']:
                print(f"Available Balance: {self.balance}")

    def transfer(self, recipient):
        amount = int(input('Enter transfer_amount: '))
        acc_no = int(input('Enter account no to transfer: '))
       
        for user in self.account_list:
            if acc_no == user['acc_no']:
                if amount <= self.balance:
                    self.balance -= amount
                    recipient.balance += amount
                    self.transactions.append(f"transfer: {amount}")
                    self.transactions.append(f"available balance: {self.balance}")
                else:
                    print('The bank is bankrupt...!')

    def transaction_history(self):
        print()
        print(f"{'*'*10} Transaction History {'*'*10}")
        for transaction in self.transactions:
            print(transaction)

    def take_A_loan(self):
        loan_amount = self.balance * 2
        self.balance += loan_amount
        self.bank_balance -= loan_amount
        self.total_loan_amount += loan_amount
        self.transactions.append(f"take a loan: {loan_amount}")



class Admin(User):
    def create_account(self):
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        acc_no = int(input('Enter your account no: '))
        new_user = Person(email, password, acc_no)
        self.account_list.append(vars(new_user))
        print('Account Created Successfully...!')

    def check_bank_balance(self):
        print()
        print()
        print(f"Bank available Balance: {self.bank_balance}")

    def check_loan_amount(self):
        print()
        print()
        print(f"Bank total loan amount: {self.total_loan_amount}")

    def control_loan(self):
        if self.balance * 2 >= self.bank_balance:
            self.take_A_loan()
        else:
            print("At this moment, tha bank is not providing loan...!")
    



# bank = Bank()
# user_1 = User()
# user_2 = User()


# user_1.create_account()
# user_1.deposit()
# user_1.withdraw()
# user_1.check_available_balance()
# user_2.create_account()
# user_1.transfer(user_2)
# user_1.transaction_history()
# user_1.check_available_balance()




#---------Global Section----------
while True:
    b = Bank()
    u = User()
    a = Admin()

    print(f"1. User\n2. Admin")

    user_input = int(input('Enter your choice: '))

    if user_input == 1:
        print(f"1. Create an account\n2. Login\n")
        user_input = int(input('Enter your choice: '))
        if user_input == 1:
            u.create_account()
        elif user_input == 2:
            email = input('Enter your email: ')
            password = input('Enter your password: ')

            for user in b.get_user():
                if user['email'] == email and user['password'] == password:
                    while True:
                        print(f"{'*'*10} Welcome to our Bank\n")
                        print(f"1. Deposit\n2. Withdraw\n3. Check Available balance\n4. transfer\n5. Transaction history\n6. Take a loan\n7. logout")
                        a = int(input('Enter your choice: '))

                        if a == 7:
                            break
                        elif a == 1:
                            u.deposit()
                        elif a == 2:
                            u.withdraw()
                        elif a == 3:
                            u.check_available_balance()
                        elif a == 4:
                            u.transfer()
                        elif a == 5:
                            u.transaction_history()
                        elif a == 6:
                            u.take_A_loan()
                else:
                    print('No user Found')
    
    elif user_input == 2:
        print(f"1. Create an account\n2. Login\n")
        user_input = int(input('Enter your choice: '))

        if user_input == 1:
            a.create_account()
        elif user_input == 2:
            email = input('Enter your email: ')
            password = input('Enter your password: ')

            for user in b.get_user():
                if user['email'] == email and user['password'] == password:
                    while True:
                        print(f"{'*'*10} Welcome to our Bank\n")
                        print(f"1. Check bank balance\n2. Check loan amount\n3. control loan\n4. logout")

                        x = int(input('Enter your choice: '))
                        if x == 4:
                            break
                        elif x == 1:
                            a.check_bank_balance()
                        elif x == 2:
                            a.check_loan_amount()
                        elif x == 3: 
                            a.control_loan()

                else:
                    print("No Admin Found")







