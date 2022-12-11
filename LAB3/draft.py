from enum import Enum

class Currency(Enum):
    USD = 468
    RUB = 7.5
    KZT = 1
    EUR = 460

class BankAccount:
    def __init__(self, name , surname , amount_of_money, currency) -> None:
        self.name = name
        self.surname = surname
        self.amount_of_money = amount_of_money
        self.currency = currency

    def get_currency(self):
        return self.currency
    def set_currency(self, new_currency):
        self.currency = new_currency
    def __str__(self) -> str:
        return f'Bank account of {self.name} {self.surname} who has {self.amount_of_money} money in {self.currency}'

    def add_to_bank_account(self, value):
        self.amount_of_money += value
    def substract_from_bank_account(self, value):
        if value <= self.amount_of_money:
            self.amount_of_money -= value
        else:
            return "Operation denied. Not enough money! \n"
    def money_conversion(self, new_currency):
        
        if self.currency == Currency.EUR:
            if new_currency == Currency.KZT:
                self.currency = Currency.KZT
                self.amount_of_money *= Currency.KZT.value
            elif new_currency == Currency.RUB:
                self.currency = Currency.RUB
                self.amount_of_money *= 150
            elif new_currency == Currency.USD:
                self.currency = Currency.USD
                self.amount_of_money *= 1.
        if self.currency == Currency.KZT:
            if new_currency == Currency.EUR:
                
        
            
    