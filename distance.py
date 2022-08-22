from metrics import MetricsCalculator


class Levenshtein(MetricsCalculator):

    def compute_distance(self, source, target):
        n = len(source)
        m = len(target)
        matrix = self.__create_matrix(n, m)
        for j in range(0, m+1):
            matrix[0][j] = j
        for i in range(1, n+1):
            matrix[i][0] = i
            for k in range(1, m+1):
                if source[i-1] == target[k-1]:
                    replace_cost = 0
                else:
                    replace_cost = 1
                matrix[i][k] = min(matrix[i][k-1] + 1,
                                        matrix[i-1][k] + 1,   #
                                        matrix[i-1][k-1] + replace_cost)  # Replace
        return matrix[-1][-1]

    @staticmethod
    def __create_matrix(n, m):
        row = [0] * (m+1)
        matrix = []
        for i in range(0, n+1):
            matrix.append(row[:])
        return matrix







distancer = Levenshtein()
# print(distancer.compute_distance("", "löffel"))
# print(distancer.compute_distance("sitting", "kitten"))

# distancer2 = DistanceCalculator()
# print(distancer2.compute_distance("sit", "kit"))
# dist3 = DistanceCalculator()
# print(distancer is dist3)


# wordlist = ["help", "hell", "hello", "loop", "troop"]

# for word in wordlist[1:]:
#     print((wordlist[0], word), calculate_distance(wordlist[0], word))
