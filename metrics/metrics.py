# Olha Svezhentseva
# 16.08.2022

from abc import ABC, abstractmethod

class SingletonClass:
    """A class that allows to create only one instance"""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


class WordDistanceCalculator(ABC, SingletonClass):
    """A class to calculate distance. Only one instance can be created"""
    @abstractmethod
    def compute_distance(self, source, target):
        pass

