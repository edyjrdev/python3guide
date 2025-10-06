#!/usr/bin/env python

class AccountBalanceError(Exception):
    def __init__(self, account_balance, amount):
        super().__init__(account_balance, amount)
        self.account_balance = account_balance
        self.amount = amount

    def __str__(self):
        return "Account balance too low (need {} USD more)".format(self.amount - self.account_balance)


class Account:
    def __init__(self, amount):
        self.account_balance = amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            raise AccountBalanceError(self.account_balance, amount)
        self.account_balance -= amount


if __name__ == "__main__":
    a = Account(1000)

    try:
        a.withdraw(2000)
    except AccountBalanceError as e:
        print("Account balance: {} USD".format(e.account_balance))
        print("Unable to withdraw {} USD".format(e.amount))

    a.withdraw(2000)
