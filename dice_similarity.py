from metrics import WordDistanceCalculator


class DiceDistanceCalculator(WordDistanceCalculator):

    def compute_distance(self, word1, word2):
        source__bigr = self.__get_bigrams(word1)
        target_bigr = self.__get_bigrams(word2)
        intersect = self.__compute_intersection(source__bigr,target_bigr)
        result = (2 * intersect)/(len(source__bigr) + len(target_bigr))
        return round(1 - result, 2)

    @staticmethod
    def __get_bigrams(word):
        bigrams = set()
        for i in range(0, len(word) - 1):
            bigrams.add(word[i: i + 2])
        return bigrams

    @staticmethod
    def __compute_intersection(source_bigrams, target_bigrams):
        return len(source_bigrams & target_bigrams)





# coefficient = DiceSimilarity()
# print(coefficient.compute_similarity("night", "nacht"))
# print(coefficient.compute_similarity("nanu", "nana"))
# print(coefficient.compute_similarity("nana", "nana"))