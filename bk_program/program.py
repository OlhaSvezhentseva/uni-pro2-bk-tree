# Olha Svezhentseva
# 24.08.2022

from __future__ import annotations

import argparse

from derewo_words import extract_words
from tree import Tree, METRIC_CLASSES
from graph_visualisation import create_vis

import typing
if typing.TYPE_CHECKING:
    from metrics.metrics import WordDistanceCalculator

from nltk import word_tokenize


def execute_command(word: str, d: float, tree: Tree) -> list:
    result = tree.find_matches(tree.main_root, word, float(d))
    return result


def run_interactive_mode(tree: Tree) -> None:
    while True:
        user_input = input().strip().lower()
        if user_input == "":
            break
        user_input = word_tokenize(user_input)
        word = user_input[0]
        d = user_input[1]
        print(execute_command(word, d, tree))


def create_tree(distance_calc: WordDistanceCalculator, words: list) -> Tree:
    tree = Tree(distance_calculator=distance_calc, words=words)
    tree.serialize("main_root", "distance_calcualtor")
    reconstructed_tree = Tree.deserialize("main_root", "distance_calcualtor")
    return reconstructed_tree


def show_tree_info(tree: Tree) -> None:
    print(f'Number of nodes: {tree.get_number_nodes(tree.main_root)}')
    print(f'Tree depth: {tree.get_tree_depth(tree.main_root)}')


def initialize_program(words_file: str, calculator_type: str) -> tuple:
    words = extract_words(words_file)
    distance_calc = METRIC_CLASSES[calculator_type]()
    return words, distance_calc


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    parser.add_argument("--metric",  nargs='?', default="edit")
    args = parser.parse_args()

    words, distance_calc = initialize_program(args.file, args.metric)

    reconstructed_tree = create_tree(distance_calc, words[:10])
    create_vis(reconstructed_tree.main_root)
    show_tree_info(reconstructed_tree)
    run_interactive_mode(reconstructed_tree)
