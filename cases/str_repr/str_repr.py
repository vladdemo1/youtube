"""This module contains main info about __str__ and __repr__ in Python"""


class Person:

    def __init__(self, name='Bob', age=30):
        self.name = name
        self.age = age

    def hello(self):
        print(f'Hello, {self.name}')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.age})"


me = Person('Vlad', 21)

print(me)
