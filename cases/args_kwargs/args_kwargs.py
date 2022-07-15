"""This module contains main info about *args and **kwargs in Python"""

# *args -> adds arguments to a tuple
# **kwargs -> adds named arguments to a dictionary


def colors(first, second):
    if first == second:
        print(first)


main_colors = ('blue', 'blue')

colors(*main_colors)


def info(first, second=2, *args, **kwargs):
    print(f'First: {first}')
    print(f'Second: {second}')

    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(f'Key: {key} and value: {value}')


personal_tuple = ('vlad', 21, 'Python', 'YouTube', 1000)

personal_dict = dict(car='Tesla', video='Args-Kwargs')

info(*personal_tuple, **personal_dict)
