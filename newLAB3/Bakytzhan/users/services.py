from typing import Optional

from models import User
from repositories import UserRepositories


class UserServices:
    repos: UserRepositories

    def __init__(self, repos: UserRepositories):
        self.repos = repos

    def create_user(self, username: str, password: str) -> None:
        self.repos.create_user(username, password)

    def get_user(self, username: str, password: str)-> Optional[User]:
        return self.repos.get_user(username, password)

    @staticmethod
    def _send_email_verification(email:str)->None:
        print(f"Email has been sende to {email}")
