from abc import ABC

class SingletonClass:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


class MetricsCalculator(ABC, SingletonClass):
    def compute_distance(self, source, target):
        pass