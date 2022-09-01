# Olha Svezhentseva
# 24.08.2022

from __future__ import annotations

import argparse


from bk_program.tree import Tree, METRIC_CLASSES
from bk_program.graph_visualisation import Visualisation

import typing
if typing.TYPE_CHECKING:
    from metrics.metrics import WordDistanceCalculator

from nltk import word_tokenize

class BKSearcher:
    "A class respon"

    def __init__(self, words_file: str, calculator_type: str):
        self.words = self._read_words(words_file)
        self. distance_calc = METRIC_CLASSES[calculator_type]()
        self. vis_required = self._visualisation_required()
        self.tree = self.create_tree()

    def execute_command(self, word: str, d: float) -> list:
        """The method returns all matches found in a tree based on user's query."""
        result = self.tree.find_matches(word, float(d))
        return result

    def create_tree(self) -> Tree:
        """The method creates a tree and returns its reconstructed version."""
        tree = Tree(distance_calculator=self.distance_calc, words=self.words)
        tree.serialize("main_root", "distance_calcualtor")
        reconstructed_tree = Tree.deserialize("main_root", "distance_calcualtor")
        return reconstructed_tree

    # Spend to much time checking length of words?
    def _visualisation_required(self):
        return len(self.words) <= 50

    @staticmethod
    def _read_words(path):
        with open(path) as file_in:
            return file_in.read().split("\n")





class Chat:


    WARNINGS = {"invalid length": "Input must be in the following format: word number. Try again.",
                "invalid word": "Your input must begin with a string. Try again.",
                "invalid distance": "After a word there must be a number. Try again."
                }

    def __init__(self, bot):
      self.bot = bot

    def show_warning_message(self, status):
        """The method prints a warning to the user."""
        return self.WARNINGS[status]

    def run_interactive_mode(self) -> None:
        """
        The method is responsible for continuous flow of the program,
        so that user's input is always awaited.
        """
        print(f"The program will now switch to interactive mode. "
              "Empty input will stop the program.")
        while True:
            print(f"Type a word and the maximum distance a string can be from your word "
                  "and will still be returned. "
                  "There must be a space between the word and the number.")
            user_input = input().strip().lower()
            if user_input == "":
                print("Bye!")
                break
            status, *result = self.check_input(user_input)
            if status:
                print(f"Results: {self.bot.execute_command(result[0], result[1])}")
            else:
                print(self.show_warning_message(result[0]))

    def check_input(self, user_input: str) -> str or tuple:
        """The method processes user's input. """
        user_input = word_tokenize(user_input)
        if not self._valid_length(user_input):
            return False, "invalid length"

        word = user_input[0]
        d = user_input[1]

        if not self._not_number(word):
            return False, "invalid word"

        if not self._valid_distance(d):
            return False, "invalid distance"
        return True, word, d

    @staticmethod
    def _valid_length(query: str) -> bool:
        """The method checks input's length."""
        return len(query) == 2

    @staticmethod
    def _not_number(word: str) -> bool:
        """The method checks that a word doens't solely consist of numbers."""
        try:
            int(word)
        except ValueError:
            return True
        return False

    @staticmethod
    def _valid_distance(d) -> bool:
        """The method checks that d can be converted to a float."""
        try:
            float(d)
        except ValueError:
            return False
        return True









def show_tree_info(tree: Tree, metric) -> None:
    """The method prints information about a given tree."""
    print(f"----The tree has been built. -----")
    print(f"It is based on {metric} distance. "
          f"All the subnodes on the edge numbered n have {metric} distance of n to the parent node.")
    print(f'Number of nodes: {tree.get_number_nodes(tree.main_root)}')
    print(f'Tree height: {tree.get_tree_height(tree.main_root)}')








if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    parser.add_argument("--metric",  nargs='?', default="edit")


    args = parser.parse_args()
    bksearcher = BKSearcher(args.file, args.metric)
    show_tree_info(bksearcher.tree, args.metric)

    # Visualisation
    vis = Visualisation()
    vis.create_vis(bksearcher.tree,  bksearcher.vis_required)

    chat = Chat(bksearcher)
    chat.run_interactive_mode()





# Visualisation required as a parameter in argparse
# if __name__ == "__main__":
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--file", type=str)
#     parser.add_argument('--vis', action='store_true')
#     parser.add_argument("--metric",  nargs='?', default="edit")
#
#
#     args = parser.parse_args()
#     print(args)
#     words, distance_calc = initialize_program(args.file, args.metric)
#
#     reconstructed_tree = create_tree(distance_calc, words)
#
#     show_tree_info(reconstructed_tree)
#
#     # Visualisation
#     # create_vis(reconstructed_tree.main_root)
#     vis = Visualisation()
#     print(args.vis)
#     vis.create_vis(reconstructed_tree.main_root, args.vis)
#     run_interactive_mode(reconstructed_tree)



