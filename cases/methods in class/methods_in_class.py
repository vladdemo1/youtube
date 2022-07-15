"""This module contains class with normal method, static and class methods"""


class Restaurant:
    """This class represent different normal, static and class methods"""

    NAME = 'Grove Street Pizza'

    def __init__(self, address: str, rating: int):
        self.address = address
        self.rating = rating

    def get_full_info(self) -> str:
        """Full info about current restaurant"""
        return f'Restaurant {self.NAME} located at {self.address} and has a rating - {self.rating}.'

    @classmethod
    def get_name_restaurant(cls) -> str:
        """Get current name restaurant"""
        return f'The one and only restaurant -> {cls.NAME}.'

    @staticmethod
    def entry_by_age(age: int) -> bool:
        """Check age person for entry to current restaurant"""
        if 18 <= age <= 100:
            return True
        return False


Restaurant.get_name_restaurant()
Restaurant.entry_by_age(10)

Restaurant('Str. 10', 10).get_full_info()
