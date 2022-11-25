
class Bank_acc:
    def __init__(self,name , money, valuta) -> None:
        self.name = name
        self.money = money
        self.valuta = valuta
    def add_to_bank_account(self,sum):
        self.money+= sum
    def substract(self, sum):
        self.money-=sum
    def to_USD(self, new_valuta):
        if self.valuta == "KZT" and new_valuta == "USD":
            self.money /= 425
            self.valuta = new_valuta
    def to_KZT(self, new_valuta):
        if self.valuta == "USD" and new_valuta == "KZT":
            self.money *= 425
            self.valuta = new_valuta
    
me = Bank_acc("Bakytzhan", 1000, "KZT")
me.to_USD("USD")
print(me.money)


