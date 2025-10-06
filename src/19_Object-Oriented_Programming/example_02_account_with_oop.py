#!/usr/bin/env python

class Account:
    def __init__(self, owner, account_number, account_balance, max_daily_turnover=1500):
        self.owner = owner
        self.account_number = account_number
        self.account_balance = account_balance
        self.max_daily_turnover = max_daily_turnover
        self.turnover_today = 0

    def money_transfer(self, destination, amount):
        # Here the test takes place whether the transfer is possible
        if amount < 0 or self.turnover_today + amount > self.max_daily_turnover or destination.turnover_today + amount > destination.max_daily_turnover:
            # Transfer impossible
            return False
        else:
            # Everything OK - Let's go
            self.account_balance -= amount
            self.turnover_today += amount
            destination.account_balance += amount
            destination.turnover_today += amount
            return True

    def deposit(self, amount):
        if amount < 0 or self.turnover_today + amount > self.max_daily_turnover:
            # Daily limit exceeded or invalid amount
            return False
        else:
            self.account_balance += amount
            self.turnover_today += amount
            return True

    def withdraw(self, amount):
        if amount < 0 or self.turnover_today + amount > self.max_daily_turnover:
            # Daily limit exceeded or invalid amount
            return False
        else:
            self.account_balance -= amount
            self.turnover_today += amount
            return True

    def show(self):
        print("Account of {}".format(self.owner))
        print("Current account balance: {:.2f} USD".format(self.account_balance))
        print("(Today already {:.2f} of {} USD turned over)".format(self.turnover_today, self.max_daily_turnover))



if __name__ == "__main__":
    a1 = Account("Steve Miller", 567123, 12350.0)
    a2 = Account("John Smith", 396754, 15000.0)
    a1.money_transfer(a2, 160)
    a2.money_transfer(a1, 1000)
    a2.money_transfer(a1, 500)
    a2.deposit(500)
    a1.show()
    a2.show()
