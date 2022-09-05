# Olha Svezhentseva
# 16.08.2022

from abc import ABC, abstractmethod
from typing import Union


class Singleton:
    """A class that allows to create only one instance."""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class WordDistanceCalculator(ABC, Singleton):
    """A class to calculate distance."""

    @abstractmethod
    def compute_distance(self, source: str, target: str) -> Union[float, int]:
        pass
