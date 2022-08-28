# Olha Svezhentseva
# 24.08.2022

from __future__ import annotations

import argparse


from bk_program.tree import Tree, METRIC_CLASSES
from bk_program.graph_visualisation import create_vis

import typing
if typing.TYPE_CHECKING:
    from metrics.metrics import WordDistanceCalculator

from nltk import word_tokenize


def execute_command(word: str, d: float, tree: Tree) -> list:
    """The method returns all matches that found in a tree based on user's query"""
    result = tree.find_matches(tree.main_root, word, float(d))
    return result


def run_interactive_mode(tree: Tree) -> None:
    """The method is responsible for continuous flow of the program, so that user's input is always awaited"""
    while True:
        user_input = input().strip().lower()
        if user_input == "":
            break
        user_input = word_tokenize(user_input)
        word = user_input[0]
        d = user_input[1]
        print(execute_command(word, d, tree))


def create_tree(distance_calc: WordDistanceCalculator, words: list) -> Tree:
    """The method creates a tree an returns its reconstructed version"""
    tree = Tree(distance_calculator=distance_calc, words=words)
    tree.serialize("main_root", "distance_calcualtor")
    reconstructed_tree = Tree.deserialize("main_root", "distance_calcualtor")
    return reconstructed_tree


def show_tree_info(tree: Tree) -> None:
    """The method prints information about a given tree """
    print(f'Number of nodes: {tree.get_number_nodes(tree.main_root)}')
    print(f'Tree depth: {tree.get_tree_depth(tree.main_root)}')

def read_words(path):
    with open(path) as file_in:
        return file_in.read().split("\n")


def initialize_program(words_file: str, calculator_type: str) -> tuple:
    """The method initializes program by extracting words from a file and creating distance_calculator"""
    words = read_words(words_file)
    distance_calc = METRIC_CLASSES[calculator_type]()
    return words, distance_calc


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    parser.add_argument("--metric",  nargs='?', default="edit")
    args = parser.parse_args()
    words, distance_calc = initialize_program(args.file, args.metric)

    reconstructed_tree = create_tree(distance_calc, words)

    # Visualisation
    create_vis(reconstructed_tree.main_root)
    show_tree_info(reconstructed_tree)
    run_interactive_mode(reconstructed_tree)
