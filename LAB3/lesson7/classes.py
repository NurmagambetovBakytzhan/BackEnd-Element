import random
import string
import uuid
from typing import Optional, List


dict_person = {
    'name': 'John',
    'surname': 'Doe',
    'age': 30,
}


class Person:
    name: str = 'John'
    surname: str = 'Doe'
    age: int = 30
    _username: Optional[str] = None

    def get_full_name(self) -> str:
        return f'{self.name} {self.surname}'

    @classmethod
    def some(cls):
        return 'ge'

    @classmethod
    def generate_username(cls, length: int = 8) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    @staticmethod
    def generate_username_v2(length: int = 8) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def set_username(self, username: str) -> None:
        if len(username) > 8:
            print('invalid username')
            return

        self._username = username

    @property
    def username(self) -> str:
        return self._username

    def __repr__(self) -> str:
        return self.get_full_name()


person = Person()
print(person)

person.name = 'Mike'
print(person)

person.set_username(username=Person.generate_username_v2())
print(person.username)


def filter_persons(persons: List[Person]) -> List[Person]:
    return [p for p in persons if p.age > 20]


p1 = Person()
p1.age = 23

p2 = Person()
p2.age = 20

p3 = Person()
p3.age = 31

p4 = Person()
p4.age = 12

new_persons = [p1, p2, p3, p4]

filtered_persons = filter_persons(persons=new_persons)
print(filtered_persons)


person.id = uuid.uuid4()
print(person.id)
