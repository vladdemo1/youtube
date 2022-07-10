"""This module contains basic information about bool - True and False in Python"""


standard = True
designation = False

true = 1
false = 0

negative_true = -55
float_false = 0.0

big_true_value = 1234567890
none_false = None

empty_list = list()
fill_tuple = (1, 14, 5, 10,)

len(empty_list)

cars = ('Tesla', 'Dodge', 'BMW',)

if cars:
    print('We have cars to buy!')
else:
    print('Not this time.')

weekends = dict()

if weekends:
    print('We can rest!')
else:
    print('Now is the time!')


class CustomBool:
    """Test class with return boolean"""

    def __init__(self, price=0):
        self.price = price

    def __bool__(self) -> bool:
        if self.price != 0:
            return True
        return False


class_bool = CustomBool()

if class_bool:
    print('Like True')
else:
    print('Like False')
