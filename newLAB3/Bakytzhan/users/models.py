import hashlib
from enum import Enum
from typing import List


class Currency(Enum):
    KZT = "KZT"
    USD = "USD"
    RUB = "RUB"

exchange_rate = {
    ('KZT', 'USD'): 1 / 480,
    ('KZT', 'RUB'): 1 / 7,
    ('KZT', 'EUR'): 0.002,
    ('USD', 'KZT'): 480,
    ('USD', 'RUB'): 480 / 7,
    ('USD', 'EUR'): 480 / 500,
    ('RUB', 'KZT'): 7,
    ('RUB', 'EUR'): 500 / 7,
    ('RUB', 'USD'): 480 / 7,
    ('EUR', 'KZT'): 500,
    ('EUR', 'RUB'): 500 / 7,
    ('EUR', 'USD'): 500 / 480,
}


class Wallet:
    cash_amount: int
    currency: Currency

    def __init__(self, currency: Currency):
        self.currency = currency

    def add_cash_amount(self, val: int):
        self.cash_amount += val

    def set_cash_amount(self, val: int):
        self.cash_amount = val

    def __repr__(self):
        return f'{self.currency} {self.cash_amount}'


class User:
    username: str
    __password: str
    wallets: List[Wallet]

    def __init__(self, username: str):
        self.username = username

    def add_to_bank_account(self, cash_amount: int, currency: Currency):
        self.filter_wallets(currency).add_cash_amount(cash_amount)

    def substract_from_bank_account(self, cash_amount: int, currency: Currency):
        self.filter_wallets(currency).add_cash_amount(-cash_amount)

    def open_wallet(self, currency: Currency):
        new_wallet = Wallet(currency)
        if self.filter_wallets(currency) is not None:
            print("Wallet with this currency already exists")
            return
        self.wallets.append(new_wallet)
        print("New wallet has been created")

    def filter_wallets(self, currency: Currency):
        # return [w for w in self.wallets if w.currency == currency][0]
        return next(w for w in self.wallets if currency == w.currency), None

    def money_conversion(self, currency_from : Currency, currency_to : Currency):
        if self.filter_wallets(currency_from) is not None and self.filter_wallets(currency_to) is not None:
            for k, v in exchange_rate.items():
                if k[0] == currency_from.name and k[1] == currency_to.name:
                    amount = self.filter_wallets(currency_from).cash_amount * v
                    self.filter_wallets(currency_to).add_cash_amount(amount)
                    self.filter_wallets(currency_from).set_cash_amount(0)
                    return
            print("Error!")

    def set_password(self, password: str):
        self.__password = self._hash_password(password)

    def check_password(self, password: str) -> bool:
        return self.__password == self._hash_password(password)

    @staticmethod
    def _hash_password(password: str):
        return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()

    def __repr__(self):
        return f'{self.username} {self.__password} {self.wallets}'
