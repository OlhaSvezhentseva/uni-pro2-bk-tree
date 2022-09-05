# Olha Svezhentseva
# 16.08.2022

from .metrics import WordDistanceCalculator


class Node:
	"""A class to represent a node of a tree."""

	def __init__(self, name: str):
		self.name = name
		self.children = {}

	def __str__(self) -> str:
		return self.name

	def insert_word(self, word: str, root: "Node", distance_calculator: WordDistanceCalculator) -> None:
		"""
		The method creates an object of class Node for a specific word
		and inserts it into a dictionary of children of a corresponding root.
		"""
		distance = distance_calculator.compute_distance(word, root.name)
		if distance not in root.children:
			root.children[distance] = Node(word)
		else:
			self.insert_word(word, root.children[distance], distance_calculator)
