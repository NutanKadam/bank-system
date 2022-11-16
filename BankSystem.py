class User:
    def __init__(self,name,age,gender,bank_name,balance):
        self.name=name
        self.age=age
        self.gender=gender
        self.bank_name=bank_name
        self.balance=balance

class Bank(User):
    def __init__(self, name, age, gender,bank_name,balance):
        super().__init__(name, age, gender,bank_name,balance)
        self.withdraw_money=0
        self.deposite_amt=0
        self.menu()

    def menu(self):
        select = input("""what would you like know ?? 
               1.Deposite
               2.Withdraw
               3.View Deatils
               4.Exit
               """)
        if select == '1':
            self.deposite()
        elif select == '2':
            self.withdraw()
        elif select=='3':
            self.show_detail()
        elif select=='4':
            print("Thanks for using Our Service")
        else:
            print("Thanks")

    def deposite(self):
        # user passing deposite amount from outside the class but folowing stmt take value from user and it override the value here
        #self.deposite_amt = int(input("deposite your amount:"))
        self.balance = self.balance + self.deposite_amt
        print(f"{self.deposite_amt} Rupees amount has been deposited successfully")
        self.menu()

    def withdraw(self):
        if self.balance != 0:
            # user withdraw money from outside the class but folowing stmt take withdraw value from user and it override the passed value here
            # so user can't make changes directly the coder are asking amount then code perform operation at the backend
            self.withdraw_money = int(input("enter amount you want to withdraw"))

            if self.balance<self.withdraw_money:
                print(f'You entered {self.withdraw_money}large amount than available balanace, Please Enter amount less than {self.balance}')
                self.withdraw()

            elif self.balance>=self.withdraw_money:
                self.balance = self.balance - self.withdraw_money
                if self.balance<=20:
                    print(f"Account Balance should contain at least 20 Rupees and you withdrawing {self.withdraw_money},"
                          f" Please withdraw less than {self.withdraw_money}")
                    self.balance=self.balance+self.withdraw_money
                    self.withdraw()

                else:
                    daily_withdraw_limit=50
                    if self.balance>=20:
                        if self.withdraw_money>daily_withdraw_limit:
                            print(f'Daily Limit of withdrawlation is: {daily_withdraw_limit} and You trying to withdraw {self.withdraw_money}, Withdraw Again!')
                            self.balance = self.balance + self.withdraw_money
                            self.withdraw()
                        else:
                            print(f'withdraw {self.withdraw_money} Rupees Successfully and Available balance is {self.balance}')
            else:
                pass
        else:
            print('Your Account has 0 Balanace')
            self.menu()



    def Available_bal(self):
        if self.balance!=0:
            available_bal=self.balance
            return available_bal
        else:
            print('Your Account has 0 Balanace')

    def show_detail(self):
        print(f'User details:\n The name is: {self.name} | Age is: {self.age} | Gender is: {self.gender}')
        # Withdraw amount: {self.balance}\n
        print(f'Account Details:\n Bank_name is: {self.bank_name} | Total_amount was: {self.balance} | Deposite amount is:{self.deposite_amt} '
              f'| Withdraw amount: {self.withdraw_money} | remaining Balance is: {self.Available_bal()}')
        self.menu()

reshh=Bank( 'Reshh',25,'Female','Bank Of India',100)
# reshh.withdraw_money=500
# reshh.withdraw()
# reshh.deposite_amt=5000
# reshh.deposite()
# reshh.show_detail()
""" The parent class User object can't access Child class Bank attributes bcoz it doesn't have features of child class"""
# User.deposite_amt=400


