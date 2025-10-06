#!/usr/bin/env python

class ManagedMoneyAmount:
    def __init__(self, initial_amount):
        self.amount = initial_amount

    def deposit_possible(self, amount):
        return True

    def withdraw_possible(self, amount):
        return True

    def deposit(self, amount):
        if amount < 0 or not self.deposit_possible(amount):
            return False
        else:
            self.amount += amount
            return True

    def withdraw(self, amount):
        if amount < 0 or not self.withdraw_possible(amount):
            return False
        else:
            self.amount -= amount
            return True

    def show(self):
        print("Amount: {:.2f}".format(self.amount))


class GeneralAccount(ManagedMoneyAmount):
    def __init__(self, customer_data, account_balance):
        super().__init__(account_balance)
        self.customer_data = customer_data

    def money_transfer(self, destination, amount):
        if self.withdraw_possible(amount) and destination.deposit_possible(amount):
            self.withdraw(amount)
            destination.deposit(amount)
            return True
        else:
            return False

    def show(self):
        self.customer_data.show()
        super().show()


class GeneralAccountWithDailyTurnover(GeneralAccount):
    def __init__(self, customer_data, account_balance, max_daily_turnover=1500):
        super().__init__(customer_data, account_balance)
        self.max_daily_turnover = max_daily_turnover
        self.turnover_today = 0.0

    def transfer_possible(self, amount):
        return (self.turnover_today + amount <= self.max_daily_turnover)

    def withdraw_possible(self, amount):
        return self.transfer_possible(amount)

    def deposit_possible(self, amount):
        return self.transfer_possible(amount)

    def deposit(self, amount):
        if super().deposit(amount):
            self.turnover_today += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if super().withdraw(amount):
            self.turnover_today += amount
            return True
        else:
            return False

    def show(self):
        super().show()
        print("Today already {:.2f} of {:.2f} USD turned over".format(self.turnover_today, self.max_daily_turnover))


class CheckingAccountCustomerData:
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number

    def show(self):
        print("Owner:", self.owner)
        print("Account number:", self.account_number)


class CheckingAccountWithDailyTurnover(GeneralAccountWithDailyTurnover):
    def __init__(self, owner, account_number, account_balance, max_daily_turnover=1500):
        customer_data = CheckingAccountCustomerData(owner, account_number)
        super().__init__(customer_data, account_balance, max_daily_turnover)


class ManagedCashAmount(ManagedMoneyAmount):
    def __init__(self, cash_amount):
        if cash_amount < 0:
           cash_amount = 0
        super().__init__(cash_amount)

    def withdraw_possible(self, amount):
        return (self.amount >= amount)


class Wallet(ManagedCashAmount):
    # TODO: Special methods for a wallet
    pass


class Safe(ManagedCashAmount):
    # TODO: Special methods for a safe
    pass


class CheckingAccount(GeneralAccount):
    def __init__(self, owner, account_number, account_balance):
        customer_data = CheckingAccountCustomerData(owner, account_number)
        super().__init__(customer_data, account_balance)


class NumberedAccountCustomerData:
    def __init__(self, identification_number):
        self.identification_number = identification_number

    def show(self):
        print("Identification number:", self.identification_number)


class NumberedAccount(GeneralAccount):
    def __init__(self, identification_number, account_balance):
        customer_data = NumberedAccountCustomerData(identification_number)
        super().__init__(customer_data, account_balance)


class NumberedAccountWithDailyTurnover(GeneralAccountWithDailyTurnover):
    def __init__(self, account_number, account_balance, max_daily_turnover):
        customer_data = NumberedAccountCustomerData(account_number)
        super().__init__(customer_data, account_balance, max_daily_turnover)


if __name__ == "__main__":
    print("### First Example")
    a1 = CheckingAccountWithDailyTurnover("Steve Miller", 567123, 12350.0)
    a2 = CheckingAccountWithDailyTurnover("John Smith", 396754, 15000.0)
    a1.money_transfer(a2, 160)
    a2.money_transfer(a1, 1000)
    a2.money_transfer(a1, 500)
    a2.deposit(500)
    a1.show()
    a2.show()

    print()
    print("### Second Example")
    na1 = NumberedAccount(113427613185, 5000)
    na2 = NumberedAccountWithDailyTurnover(45657364234, 12000, 3000)
    na1.withdraw(1000)
    na2.deposit(1500)
    na1.money_transfer(na2, 2000)
    na1.show()
    na2.show()



