import sys

from users.handlers import UserHandlers
from users.repositories import UserRepositories
from users.services import UserServices
from users.models import Currency


def str_to_enum(currency: str):

    if currency == "KZT":
        return Currency.KZT
    elif currency == "RUB":
        return Currency.RUB
    else:
        return Currency.USD

def init():

    user_repos = UserRepositories()
    user_services = UserServices()
    user_handlers = UserHandlers()

    while True:
        command = input("Hello and Welcome to the our Bank System! How can I help you? \n")

        if command == 'q':
            sys.exit(0)

        if command == "sign_up":
            username, password = input('Enter username and password').split()
            user_handlers.sign_up(username, password)

        elif command == 'sign_in':
            username, password = input('Please, enter your creds: ').split()
            cur_account = user_handlers.sign_in(username=username, password=password)

        elif command == "add_to_bank_acc":
            currency = input("What currency do you want to add?")
            cash_amount = input("How much money do you want to add?")
            currency = str_to_enum(currency)
            cur_account.add_to_bank_account(cash_amount, currency)

        elif command == "substract_from_bank_acc":
            currency = input("What currency do you want to substract?")
            cash_amount = input("How much money do you want to substract?")
            currency = str_to_enum(currency)
            cur_account.add_to_bank_account(cash_amount, currency)

        elif command == "open_wallet":
            currency = input("For what currency do you want to open a new wallet?")
            currency = str_to_enum(currency)
            cur_account.open_wallet(currency)

        elif command == "money_conversion":
            currency_from = str_to_enum(input("Money from"))
            currency_to = str_to_enum(input("Money to"))
            cur_account.money_conversion(currency_from, currency_to)

        elif command == "print info":
            print(cur_account.__repr__())
        else:
            print('invalid command, try again')

if __name__ == '__main__':
    init()