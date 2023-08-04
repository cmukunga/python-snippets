class Transaction:
    def __init__(self, Trans_type, Amount, date):
        self.Trans_type = Trans_type
        self.Amount = Amount
        self.date = date

    def __str__(self):
        return f"{self.Trans_type}: {self.Amount} on {self.date}"

class Account:
    def __init__(self, Account_No, Coustomer_Name, balance):
        self.Account_No = Account_No
        self.Coustomer_Name = Coustomer_Name
        self.balance = balance
        self.Transactions = []

    def deposit(self, Amount, date):
        self.balance += Amount
        transaction = Transaction("Deposit", Amount, date)
        self.Transactions.append(transaction)

    def withdraw(self, Amount, date):
        if Amount <= self.balance:
            self.balance -= Amount
            transaction = Transaction("Withdrawal", Amount, date)
            self.Transactions.append(transaction)
        else:
            print("Insufficient account balance! please top up!!")

    def Get_balance(self):
        return self.balance

    def Statement(self):
        statement = f"Account Number: {self.Account_No}, Holder Name: {self.Coustomer_Name}\n"
        for transaction in self.Transactions:
            statement += str(transaction) + "\n"
        statement += f"Current Balance: {self.balance}"
        return statement

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, Account_No, Coustomer_Name, initial_balance):
        if Account_No not in self.accounts:
            account = Account(Account_No, Coustomer_Name, initial_balance)
            self.accounts[Account_No] = account
            print(f"Account created successfully for {Coustomer_Name} with Account Number: {Account_No}")
        else:
            print("An account with the same Account Number already exists.")

    def New_account(self, Account_No):
        if Account_No in self.accounts:
            return self.accounts[Account_No]
        else:
            print("Account not found.")
            return None

# Usage example:
if __name__ == "__main__":
    bank = Bank("Family Bank")

    bank.create_account("144566", "John Doe", 1000)
    bank.create_account("654321", "Jane Smith", 5000)

    account1 = bank.New_account("123456")
    if account1:
        account1.deposit(500, "2023-07-31")
        account1.withdraw(200, "2023-07-31")

    account2 = bank.New_account("654321")
    if account2:
        account2.deposit(1000, "2023-07-31")

    account3 = bank.New_account("987654")  # Trying to get an account that doesn't exist

    if account1:
        print("\nAccount Statement for John Doe:")
        print(account1.Statement())

    if account2:
        print("\nAccount Statement for Jane Smith:")
        print(account2.Statement())
