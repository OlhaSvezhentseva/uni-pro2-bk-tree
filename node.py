from distance import Levenshtein
from dice_similarity import DiceSimilarity
import pickle


DIST = Levenshtein()
SIM = DiceSimilarity()

class Node:

	def __init__(self, name):
		self.name = name
		self.children = {}

	def __str__(self):
		return self.name

	# def print_children(self):
	# 	for key, value in self.children.items():
	# 		print(key, value.name)

	def insert_word(self, word, root, metric):
		# Legal to do this?
		distance = 0
		if metric == "levenshtein":
			distance = DIST.compute_distance(word, root.name)
		elif metric == "dice":
			distance = SIM.compute_distance(word, root.name)
		if distance not in root.children:
			root.children[distance] = Node(word)

		else:
			self.insert_word(word, root.children[distance], metric)

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

	def save_node(self, root, nodes=None):
		if nodes is None:
			nodes = []
		nodes.append(root)
		for child in root.children.values():
			self.save_node(child, nodes)
		with open("nodes", "wb") as fp:
			pickle.dump(nodes, fp)

# where to put method "open nodes" if the tree is already built?

