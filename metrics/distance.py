# Olha Svezhentseva
# 16.08.2022

from metrics.metrics import WordDistanceCalculator


class EditDistanceCalculator(WordDistanceCalculator):
    """A class to calculate edit distance (Levenshtein distance)"""

    def compute_distance(self, source: str, target: str) -> int:
        """The method computes edit distance using dynamic programming"""
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
                matrix[i][k] = min(matrix[i][k-1] + 1, # Insert
                                        matrix[i-1][k] + 1,   # Delete
                                        matrix[i-1][k-1] + replace_cost)  # Replace
        return matrix[-1][-1]

    @staticmethod
    def __create_matrix(n: int, m: int) -> list:
        """The method creates matrix and fills it with zeroes"""
        row = [0] * (m+1)
        matrix = []
        for i in range(0, n+1):
            matrix.append(row[:])
        return matrix
