class Person:
    def __init__(self, email, password, acc_no) -> None:
        self.email = email
        self.password = password
        self.acc_no = acc_no

class Bank:
    account_list = []
    total_amount = 0
    
    def bank_info(self):
        print(f"{'*'*10} Bank Info {'*'*10}")
        print(f"Total_amount: {self.total_amount}")

class User(Bank):
    balance = 0
    def create_account(self):
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        acc_no = int(input('Enter your account no: '))
        new_user = Person(email, password, acc_no)
        self.account_list.append(vars(new_user))
        print('Account Created Successfully...!')

    def deposit(self):
        amount = int(input('Enter your deposit_amount: '))
        account_no = int(input('Enter your account no: '))
        for acc_no in self.account_list[{'acc_no'}]:
            if amount > 500 and account_no == acc_no:
                self.balance += amount
                self.total_amount += amount
            else:
                print('You have to deposit more than 500')

        

    def withdraw(self):
        amount = int(input('Enter your withdraw_amount: '))
        if amount < self.balance:
            self.balance -= amount
            self.total_amount -= amount
        else:
            print('You do not have enough money to withdraw')
    
    def check_available_balance(self):
        print(f"Available Balance: {self.balance}")

    def transfer(self):
        pass

    def transaction_history(self):
        pass


ali = User()


ali.create_account()
ali.deposit()
# ali.withdraw()
ali.check_available_balance()