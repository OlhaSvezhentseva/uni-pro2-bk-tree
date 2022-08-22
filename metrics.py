from abc import ABC, abstractmethod

class SingletonClass:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


class WordDistanceCalculator(ABC, SingletonClass):
    @abstractmethod
    def compute_distance(self, source, target):
        pass
