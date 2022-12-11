from typing import Optional, List
class Person:
    
    name: str
    surname: str
    _username: Optional[str] = None


class Car(NamedTuple):
    brand: str
    model: str
    year: int






# person = Person(name = 'Bakytzhan',surname = 'Nurmagambetov',age = 10, gender ='male')
# print(person.telegram_id)

car = Car('Kia', 'Rio', 2012)
print(car)