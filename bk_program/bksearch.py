# Olha Svezhentseva
# 01.09.2022

from typing import List
from .tree import Tree, METRIC_CLASSES


class BKSearcher:
    """A class responsible for creating and querying BK Tree."""

    def __init__(self, words_file: str, calculator_type: str):
        self.words = self._read_words(words_file)
        self. distance_calc = METRIC_CLASSES[calculator_type]()
        self. vis_required = self._visualisation_required()
        self.tree = self.create_tree()

    def execute_command(self, word: str, d: float) -> List[str]:
        """The method returns all matches found in a tree based on user's query."""
        result = self.tree.find_matches(word, d)
        return result

    def create_tree(self) -> Tree:
        """The method creates a tree and returns its reconstructed version."""
        tree = Tree(distance_calculator=self.distance_calc, words=self.words)
        tree.serialize("main_root", "distance_calculator")
        reconstructed_tree = Tree.deserialize("main_root", "distance_calculator")
        return reconstructed_tree

    def _visualisation_required(self) -> bool:
        """The method checks if visualisation is needed."""
        return len(self.words) <= 50

    @staticmethod
    def _read_words(path: str) -> List[str]:
        """The method reads words from a file"""
        with open(path) as file_in:
            return file_in.read().split("\n")
