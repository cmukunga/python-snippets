class Bank:
    account_number = 1

    def __init__(self, customer_name, current_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance = 0
        self.account_number = Bank.account_number
        Bank.account_number = Bank.account_number + 1

    def Deposit_Money(self, cash):
        self.current_balance += cash

    def Withdraw_Money(self, cash):
        if self.current_balance < cash:
            print(
                f"Sorry you current balance is low. Enter amount less than {self.current_balance}"
            )
        else:
            self.current_balance -= cash

    def My_Balance(self):
        print(f"Your current balance is : {self.current_balance}")


if __name__ == "__main__":
    customer1 = Bank("John Mark", 2500)
    customer1.Deposit_Money(2000)
    customer1.My_Balance()
    customer1.Withdraw_Money(1500)
    customer1.My_Balance()
