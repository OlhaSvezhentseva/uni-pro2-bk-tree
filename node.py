from distance import EditDistanceCalculator
from dice_similarity import DiceDistanceCalculator
import pickle


DIST = EditDistanceCalculator()
SIM = DiceDistanceCalculator()


class Node:

	def __init__(self, name):
		self.name = name
		self.children = {}

	def __str__(self):
		return self.name

	def insert_word(self, word, root, distance_calculator):
		distance = distance_calculator.compute_distance(word, root.name)
		if distance not in root.children:
			root.children[distance] = Node(word)
		else:
			self.insert_word(word, root.children[distance], distance_calculator)

	def get_tree_depth(self,root):
		if len(root.children) == 0:
			return 0
		else:
			return 1 + max(self.get_tree_depth(x) for x in root.children.values())

	def get_number_nodes(self, root):
		if len(root.children) == 0:
			return 1
		else:
			return 1 + sum(self.get_number_nodes(x) for x in root.children.values())

	def save_root(self, root):
		with open("main_root", "wb") as fp:
			pickle.dump(root, fp)

# where to put method "open nodes" if the tree is already built?

