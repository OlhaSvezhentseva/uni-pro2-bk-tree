# Olha Svezhentseva
# 16.08.2022

from distance import EditDistanceCalculator
from dice_similarity import DiceDistanceCalculator
from node import Node
from graph_visualisation import create_vis
import pickle

METRIC_CLASSES = {
	"dice": DiceDistanceCalculator,
	"edit": EditDistanceCalculator,
}


def build_tree(words, distance_calculator):
	main_root = Node(words[0])
	for word in words[1:]:
		main_root.insert_word(word, main_root, distance_calculator)
	return main_root


def find_matches(root, word, d, distance_calculator,  matches=None):
	if matches is None:
		matches = []
	dist = distance_calculator.compute_distance(word, root.name)
	if dist <= d:
		matches.append(root.name)
	for child in root.children.values():
		# if d-dist <= distance_calculator.compute_distance(word, child.name) <= d+dist:
		# Here changed d-dist ---> dist-d, because otherwise the value (untere Shranke) could be too high!
		if dist-d <= distance_calculator.compute_distance(word, child.name) <= dist+d:
			find_matches(child, word, d, distance_calculator, matches)
	return matches


metric = "edit"

# Build tree from a list of words
# with open("words", "rb") as fp:   # Unpickling
# 	words = pickle.load(fp)
# main_root = build_tree(words[:10], METRIC_CLASSES[metric]())
# print(main_root.save_root(main_root))

# Visualise tree from a pickle file where tree's root is saved
with open("main_root", "rb") as fp:
	main_root = pickle.load(fp)
create_vis(main_root)

# With message dict or without?
print(f'Number of nodes: {main_root.get_number_nodes(main_root)}')
print(f'Tree depth: {main_root.get_tree_depth(main_root)}')
print(find_matches(main_root, "hinein", 4, METRIC_CLASSES[metric]()))

