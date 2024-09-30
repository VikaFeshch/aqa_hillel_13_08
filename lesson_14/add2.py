class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

bank_acc = BankAccount(123456789, 852369741)
print(bank_acc.get_account_number())
bank_acc.set_account_number(999999999999)
print(bank_acc.get_account_number())

print(bank_acc.get_balance())
bank_acc.set_balance(7777777777777777)
print(bank_acc.get_balance())