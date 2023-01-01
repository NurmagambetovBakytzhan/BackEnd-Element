from typing import List, Optional

from models import User

# ppp
class UserRepositories:
    users: List[User] = []

    def create_user(self, username: str, password: str)-> None:
        user = User(username=username)
        user.set_password(password=password)

    def get_user(self, username: str, password: str) -> Optional[User]:
        user = next(
            (u for u in self.users if username == u.username and u.check_password(password)),
            None
        )
        if not user:
            print('User not found')
            return

        return user

    def __del__(self):
        print("User has been deleted!")