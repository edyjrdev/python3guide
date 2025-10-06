#!/usr/bin/env python

class Account:
    def __init__(self, owner, account_number, account_balance, max_daily_turnover=1500):
        self.owner = owner
        self.account_number = account_number
        self.account_balance = account_balance
        self.max_daily_turnover = max_daily_turnover
        self.turnover_today = 0

    def __eq__(self, a2):
        return self.account_number == a2.account_number



if __name__ == "__main__":
    account1 = Account("Scrooge McDuck", 1337, 9999999999999999)
    account2 = Account("Donald Duck", 1337, 1.5)
    account3 = Account("Gladstone Gander", 2674, 50000)
    print(account1 == account2)
    print(account1 == account3)









