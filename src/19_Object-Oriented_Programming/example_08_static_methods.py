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

    def junior_account(owner, account_number, account_balance):
        return Account(owner, account_number, account_balance, 20)

    junior_account = staticmethod(junior_account)


if __name__ == "__main__":
    jr = Account.junior_account("Ethan Peters", 436574, 67)
    jr.show()




