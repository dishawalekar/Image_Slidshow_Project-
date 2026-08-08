class account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def credit(self, amount):
        self.balance += amount
        print("Amount credit:", amount)

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Debit Amount:", amount)
        else:
            print("Insufficient amount")

    def show_balance(self):
        print("Account:", self.account_no, "Balance:", self.balance)



a1 = account(2000, "dish123")
a1.credit(2000)
a1.debit(5000)
a1.show_balance()


