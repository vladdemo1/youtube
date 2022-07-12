"""Different underscores in Python"""


class Home:
    """Base class about settings home"""

    return_ = {
               "public": "Without underscores like 'variable'",
               "protected": "One underscore like '_variable'",
               "private": "Two underscores like '__variable'",
               }

    def __init__(self):
        self.number = 10
        self._size = 20
        self.__price = 30


new_home = Home()

print(dir(new_home))


for _ in range(10):
    print('Make something!')

cars = ('Tesla', 'Toyota', 'BMW', 'Jeep')

first_car, _, _, second_car = cars
