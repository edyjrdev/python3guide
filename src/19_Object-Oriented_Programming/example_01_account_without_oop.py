#!/usr/bin/env python

def new_account(owner, account_number, account_balance, max_daily_turnover=1500):
    return {
        "owner": owner,
        "account_number": account_number,
        "account_balance": account_balance,
        "max_daily_turnover": max_daily_turnover,
        "turnover_today": 0
    }


def money_transfer(source, destination, amount):
    # Here we test whether the transfer is possible
    if amount < 0 or source["turnover_today"] + amount > source["max_daily_turnover"] or destination["turnover_today"] + amount > destination["max_daily_turnover"]:
        # Transfer impossible
        return False
    else:
        # Everything’s OK - Let's go
        source["account_balance"] -= amount
        source["turnover_today"] += amount
        destination["account_balance"] += amount
        destination["turnover_today"] += amount
        return True


def deposit(account, amount):
    if amount < 0 or account["turnover_today"] + amount > account["max_daily_turnover"]:
        # Daily limit exceeded or invalid amount
        return False
    else:
        account["account_balance"] += amount
        account["turnover_today"] += amount
        return True


def withdraw(account, amount):
    if amount < 0 or account["turnover_today"] + amount > account["max_daily_turnover"]:
        # Daily limit exceeded or invalid amount
        return False
    else:
        account["account_balance"] -= amount
        account["turnover_today"] += amount
        return True

def show_account(account):
    print("Account of {}".format(account["owner"]))
    print("Current account balance: {:.2f} USD".format(account["account_balance"]))
    print("(Today already {:.2f} of {} USD turned over)".format(account["turnover_today"], account["max_daily_turnover"]))


if __name__ == "__main__":
    a1 = new_account("Steve Miller", 567123, 12350.0)
    a2 = new_account("John Smith", 396754, 15000.0)
    money_transfer(a1, a2, 160)
    money_transfer(a2, a1, 1000)
    money_transfer(a2, a1, 500)
    deposit(a2, 500)
    show_account(a1)
    show_account(a2)
