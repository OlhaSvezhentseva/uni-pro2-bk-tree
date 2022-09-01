# Olha Svezhentseva
# 16.08.2022

from metrics.metrics import WordDistanceCalculator


class JaccardDistanceCalculator(WordDistanceCalculator):
    """
    A class to calculate Jaccard Distance.
    Jaccard Distance value is obtained through subtracting Jaccard coefficient from one.
    """

    def compute_distance(self, source: str, target: str) -> int:
        """The method computes distance between two words"""
        source__bigr = self.__get_bigrams(source)
        target_bigr = self.__get_bigrams(target)
        intersect = self.__compute_intersection(source__bigr,target_bigr)
        try:
            result = intersect/((len(source__bigr) + len(target_bigr)) - intersect)
        except ZeroDivisionError:
            result = 1
        return round(1 - result, 2)

    @staticmethod
    def __get_bigrams(word: str) -> set:
        """The method extracts letter bigrams from a given word."""
        bigrams = set()
        for i in range(0, len(word) - 1):
            bigrams.add(word[i: i + 2])
        return bigrams

    @staticmethod
    def __compute_intersection(source_bigrams: set, target_bigrams: set) -> int:
        """The method computes intersection between two sets."""
        return len(source_bigrams & target_bigrams)

