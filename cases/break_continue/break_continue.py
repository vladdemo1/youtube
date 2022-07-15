"""This module contains main info about break and continue in loops"""

fruits = ('peach', 'banana', 'persimmon', 'kiwi',)

disliked_fruits = ('persimmon',)

for fruit in fruits:
    if fruit in disliked_fruits:
        break
    print(fruit, end=' ')

print()

cars = {
    'Tesla model X': 1_200_000,
    'Dodge Challenger': 1_400_000,
    'BMW m3': 3_700_000,
    'Mazda 5': 300_000,
}

for car_name, price in cars.items():
    if price < 500_000 or price > 2_000_000:
        continue
    print(f'Car - {car_name}. Price: {price}')
