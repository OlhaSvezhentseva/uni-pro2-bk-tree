from distance import Levenshtein
from dice_similarity import DiceSimilarity
from node import Node
import pickle



def build_tree(words, metric):
	main_root = Node(words[0])
	for word in words[1:]:
		main_root.insert_word(word, main_root, metric)
	return main_root


def find_matches(root, word, d, metric,  matches=None):
	# Legal to do this???
	distance_calculator = None
	if matches is None:
		matches = []
	if metric == "levenshtein":
		distance_calculator = Levenshtein()
	elif metric == "dice":
		distance_calculator = DiceSimilarity()
	dist = distance_calculator.compute_distance(word, root.name)
	if dist <= d:
		matches.append(root.name)

	for child in root.children.values():
		# if d-dist <= distance_calculator.compute_distance(word, child.name) <= d+dist:
		# Here changed d-dist ---> dist-d, because otherwise the value (untere Shranke) could be too high!
		if dist-d <= distance_calculator.compute_distance(word, child.name) <= dist+d:
			find_matches(child, word, d, metric, matches)

	return matches





with open("words", "rb") as fp:   # Unpickling
	words = pickle.load(fp)

main_root = build_tree(words[:10], "dice")
# print(main_root.save_node(main_root))
# print(main_root.children)


# print(f'Number of nodes: {main_root.get_number_nodes(main_root)}')
# print(f'Tree depth: {main_root.get_tree_depth(main_root)}')
# print(find_matches(main_root, "hinein", 20))


print(find_matches(main_root, "hinein", 0.5, "dice"))



# Unpickling nodes
# with open("nodes", "rb") as fp:
# 	nodes = pickle.load(fp)
# for node in nodes:
# 	for key, value in node.children.items():
# 		print(node.name, key, value.name)