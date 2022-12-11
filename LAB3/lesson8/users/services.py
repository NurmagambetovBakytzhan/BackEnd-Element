from typing import Optional

from users.models import User
from users.repositories import UserRepositories


class UserServices:

    repositories: UserRepositories

    def __init__(self, repositories: UserRepositories):
        self.repositories = repositories

    def create_user(self, username: str, password: str) -> None:
        self.repositories.create_user(username=username, password=password)
        self._send_email_verification(email=username)

    def get_user(self, username: str, password: str) -> Optional[User]:
        return self.repositories.get_user(username=username, password=password)

    def add_money(self, user : User, money_amount: int, wallet: str):
        self.UserRepositories.add_money(user: User, money_amount: int,wallet:str)

    def get_money_info(self, user: User):
        return "hello"
    @staticmethod
    def _send_email_verification(email: str) -> None:
        print(f'send verification letter to {email}')
