from dataclasses import dataclass


class Person:
    __age: int
    full_name: str

    def __str__(self):
        return f"{self.__age}{self.full_name}"


class Driver(Person):
    experience: int

    def __str__(self):
        return f"{super.__str__()}{self.experience}"


class Engine:
    power: int
    company_name: str

    def __str__(self):
        return f"{self.power}{self.company_name}"


class Car:
    carClass: str
    engine: Engine
    driver: Driver
    mark: str

    def start(self):
        print("Let's goooo")

    def stop(self):
        print("Stop!")

    def turn_right(self):
        print("Turning right")

    def turn_left(self):
        print("Turning left")

    def __str__(self):
        return f"{self.carClass}{self.engine}{self.driver}{self.mark}"


class Lorry(Car):
    carrying: int

    def __str__(self):
        return f"{super.__str__()}{self.carrying}"


class SportCar(Car):
    speed: float

    def __str__(self):
        return f"{super.__str__()}{self.speed}"
