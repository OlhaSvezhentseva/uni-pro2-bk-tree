# Olha Svezhentseva
# 16.08.2022

import pickle
from typing import List, Optional

from . node import Node
from . import metrics


METRIC_CLASSES = {
    "jaccard": metrics.JaccardDistanceCalculator,
    "edit": metrics.EditDistanceCalculator,
}


class Tree:
    """A class to represent BK-tree."""

    def __init__(
        self,
        distance_calculator: metrics.WordDistanceCalculator,
        main_root: Optional[Node] = None,
        words: Optional[List[str]] = None
    ):
        assert main_root is not None or words is not None, \
            "Either list of words or root must be provided"
        self.distance_calculator = distance_calculator
        self.main_root = self._build_tree(words) if main_root is None else main_root

    def _build_tree(self, words: List[str]) -> Node:
        """The method builds a BK-tree based on a list of words."""
        main_root = Node(words[0])
        print(f"Total number of words: {len(words)}")
        for index, word in enumerate(words[1:], 1):
            if index % 10000 == 0:
                print(f"..processed {index} words")
            main_root.insert_word(word, main_root, self.distance_calculator)
        return main_root

    def serialize(self, root_file: str, calculator_file: str) -> None:
        """
        The method serializes main root of a tree
        and calculator used to compute the metrics.
        """
        with open(root_file, "wb") as fp:
            pickle.dump(self.main_root, fp)
        with open(calculator_file, "wb") as f:
            pickle.dump(self.distance_calculator, f)

    @classmethod
    def deserialize(cls, root_file: str, calculator_file: str) -> "Tree":
        """
        The method deserializes main root of a tree and calculator
        to reconstruct the already built tree.
        """
        with open(root_file, "rb") as fp:
            main_root = pickle.load(fp)
        with open(calculator_file, "rb") as f:
            calculator = pickle.load(f)
        return Tree(calculator, main_root)

    def get_tree_height(self, root: Node) -> int:
        """The method recursively calculates height of a tree."""
        if len(root.children) == 0:
            return 0
        else:
            return 1 + max(self.get_tree_height(x) for x in root.children.values())

    def get_number_nodes(self, root: Node) -> int:
        """The method recursively calculates number of nodes in a tree."""
        if len(root.children) == 0:
            return 1
        else:
            return 1 + sum(self.get_number_nodes(x) for x in root.children.values())

    def find_matches(
        self,
        word: str,
        d: float,
        root: Optional[Node] = None,
        matches: Optional[List[str]] = None
    ) -> List[str]:
        """The method finds all words in a tree, distance to which is less/equal than d."""
        if root is None:
            root = self.main_root
        if matches is None:
            matches = []
        dist = self.distance_calculator.compute_distance(word, root.name)
        if dist <= d:
            matches.append(root.name)
        for child_distance, child in root.children.items():
            if abs(child_distance - dist) <= d:
                self.find_matches(word, d, child, matches)
        return matches
