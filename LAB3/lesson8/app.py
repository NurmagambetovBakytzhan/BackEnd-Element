import sys

from users.handlers import UserHandlers
from users.repositories import UserRepositories
from users.services import UserServices
from LAB3.lesson8.users.models import *

def init():
    user_repositories = UserRepositories()
    user_services = UserServices(repositories=user_repositories)
    user_handlers = UserHandlers(services=user_services)

    while True:
        command = input('Enter command or enter q (quit) to exit: ')

        if command == 'q':
            sys.exit(0)

        if command == 'sign_up':
            username, password = input('Enter username and password: ').split()
            user_handlers.sign_up(username=username, password=password)

        elif command == 'sign_in':
            username, password = input('Please, enter your creds: ').split()
            our_user = user_handlers.sign_in(username=username, password=password)
            if our_user is not None:
                print(f"Welcome {username}! \n")
                while True:
                    command = input('1 : see your current wallets\n 2 : add_to_bank_account')
                    if command == '1':
                        user_handlers.get_money_info(our_user)
                    elif command == '2':
                        money_amount = int(input())
                        wallet_type = input()
                        user_handlers.add_money(our_user, money_amount, wallet_type)

        else:
            print('invalid command, try again')


if __name__ == '__main__':
    init()
