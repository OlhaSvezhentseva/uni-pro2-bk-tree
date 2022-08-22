from metrics import MetricsCalculator


class DiceSimilarity(MetricsCalculator):

    def compute_distance(self, word1, word2):
        source__bigr = self.__get_bigrams(word1)
        target_bigr = self.__get_bigrams(word2)
        intersect = self.__compute_intersection(source__bigr,target_bigr)
        result = (2 * intersect)/(len(source__bigr) + len(target_bigr))
        return 1 - round(result, 2)

    @staticmethod
    def __get_bigrams(word):
        bigrams = set()
        i = 0
        while i < len(word) -1:
            bigrams.add(word[i]+word[i+1])
            i += 1
        return bigrams

    @staticmethod
    def __compute_intersection(source_bigrams, target_bigrams):
        intersect = 0
        for element in source_bigrams:
            for bigram in target_bigrams:
                if element == bigram:
                    intersect += 1
        return intersect





# coefficient = DiceSimilarity()
# print(coefficient.compute_similarity("night", "nacht"))
# print(coefficient.compute_similarity("nanu", "nana"))
# print(coefficient.compute_similarity("nana", "nana"))