import hashlib
from enum import Enum
from typing import List


class WalletType(Enum):
    KZT = 'KZT'
    USD = 'USD'
    RUB = 'RUB'


class Wallet:
    cash_amount: int
    wallet_type: WalletType

    def __init__(self, wallet_type: WalletType):
        self.wallet_type = wallet_type

    def add_cash_amount(self, val: int):
        self.cash_amount += val

    def __repr__(self):
        return f'{self.cash_amount} {self.wallet_type} \n'


class User:
    username: str
    __password: str
    wallets: List[Wallet]

    def __init__(self, username: str):
        self.username = username

    def filter_wallets(self, wallet_type: WalletType):

        return [w for w in self.wallets if w.wallet_type == wallet_type][0]

    def add_to_bank_account(self, amount_money: int, wallet_type: WalletType):
        temp_wallet = self.filter_wallets(wallet_type)
        temp_wallet.add_cash_amount(amount_money)

    def set_password(self, password: str):
        self.__password = self._hash_password(password)

    def check_password(self, password: str) -> bool:
        return self.__password == self._hash_password(password)

    def get_money(self):
        return self.wallets.__repr__()

    def set_password(self, old_password : str, new_password: str):
        if old_password != new_password and self.check_password(old_password):
            self.__password = new_password
        else:
            return "Wrong password setting \n"

    @staticmethod
    def substract_from_bank_account(self, amount_money, wallet_type: WalletType):
        temp_wallet = self.filter_wallets(wallet_type)
        if 0 < amount_money <= temp_wallet.cash_amount:
            temp_wallet.add_cash_amount(-amount_money)
            return f"Operation is successfull! Now you have {temp_wallet.__repr__()}"
        else:
            return "Operation denied. You are poor, maaaaan! \n"

    def _hash_password(password: str):
        return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()

    def __repr__(self):
        return f'{self.username} {self.__password} with money in {self.wallets.__repr__()}'

    def money_conversion(self, wallet_type : WalletType):
        pass
