from typing import List, Optional



from LAB3.lesson8.users.models import *


class UserRepositories:
    users: List[User] = []

    def create_user(self, username: str, password: str) -> None:
        user = User(username=username)
        user.set_password(password=password)

        self.users.append(user)

    def get_user(self, username: str, password: str) -> Optional[User]:
        user = next(
            (u for u in self.users if username == u.username and u.check_password(password)),
            None
        )

        if not user:
            print('User not found')
            return

        return user

    def __del__(self, username: str):
        user = (u for u in self.users if u.username == username)
        if user:
            self.users.remove(user)
        else:
            return f"No such user {user} \n "

    def get_money_info(self, user: User):
        return next(u.get_money() for u in self.users)

    def add_money(self, user: User, money_amount: int, wallet_type: str):
        our_user = (u for u in self.users if u == user)
        if our_user:

            our_user.add_to_bank_account(money_amount, WalletType[wallet_type])
            print("Inserted! \n")
