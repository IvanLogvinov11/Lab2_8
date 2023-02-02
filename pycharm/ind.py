#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_bank_acc():
    """
    Request for bank account details with verification
    """
    while True:
        s_b_a = input("Enter the sender's bank account: ")
        if len(s_b_a) != 20 or not s_b_a.isdigit():
            print("Incorrect bank account!")
        else:
            break

    while True:
        b_a = input("Enter the beneficiary's account: ")
        if len(b_a) != 20 or not b_a.isdigit():
            print("Incorrect bank account!")
        else:
            break

    t_a = input("Enter transfer amount in ₽: ")

    return {
        "s_b_a": s_b_a,
        "b_a": b_a,
        "t_a": t_a,
    }


def display_acc(accounts):
    """"
    Display of entered bank accounts
    """
    if accounts:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 2,
            '-' * 25,
            '-' * 25,
            '-' * 10
        )
        print(line)
        print(
            '| {:^2} | {:^25} | {:^25} | {:^10} |'.format(
                "№",
                "Sender bank account",
                "beneficiary account",
                "Amount",
            )
        )
        print(line)

        for ind, requisite in enumerate(accounts, 1):
            print(
                '| {:^2} | {:^25} | {:^25} | {:^10} |'.format(
                    ind,
                    requisite.get('s_b_a'),
                    requisite.get('b_a'),
                    requisite.get('t_a'),
                )
            )
            print(line)
    else:
        print("You have no bank accounts for now!")


def sum_check(requisites, account):
    """"
    Amount of all money withdrawn
    """
    full_summa = 0
    for sender_req in requisites:

        if int(sender_req.get("s_b_a")) == int(account):
            full_summa += float(sender_req.get("t_a"))

    if full_summa == 0:
        print("This bank account does not exist")
    else:
        print(full_summa)


def help_me():
    print("Command List:\n")
    print("add - Add bank account;")
    print("list - Display a list of bank accounts;")
    print("select <bank account> -", end=" ")
    print("The withdrawn amount from account;")
    print("help - Display Help;")
    print("exit - End the program.")
    print("\n")


def invalid_com():
    print('\n')
    print(f"Invalid command use help",  file=sys.stderr)


def main():
    """
    Main function
    """
    requisites = []
    while True:

        command = input("Enter Command: ").lower()
        if command == "exit":
            break

        elif command == "add":
            requisite = get_bank_acc()
            requisites.append(requisite)

            if len(requisites) > 1:
                requisites.sort(key=lambda item: item.get("s_b_a", ""))

        elif command == "list":
            display_acc(requisites)

        elif command.startswith("select "):
            parts = command.split(" ", maxsplit=1)
            bank_acc = parts[1]
            sum_check(requisites, bank_acc)

        elif command == 'help':
            help_me()

        else:
            invalid_com()


if __name__ == '__main__':
    main()
