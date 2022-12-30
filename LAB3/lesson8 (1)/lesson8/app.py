import sys

from users.handlers import UserHandlers
from users.repositories import UserRepositories
from users.services import UserServices


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
            user_handlers.sign_in(username=username, password=password)

        else:
            print('invalid command, try again')


if __name__ == '__main__':
    init()
