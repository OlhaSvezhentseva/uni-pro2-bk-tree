import pickle
import graphviz
from node import Node
from combine import build_tree

# dot = graphviz.Digraph('BK-tree')
# dot.format = 'png'
#
#
# with open("words", "rb") as fp:   # Unpickling
# 	words = pickle.load(fp)
#
# main_root = build_tree(words[:10])
# dot.node(main_root.name)





def create_vis(main_root):
	dot = graphviz.Digraph('BK-tree')
	dot.format = 'png'
	dot.node(main_root.name)
	tree_vis(main_root, dot)



def tree_vis(root, dot):
	for dist in root.children:
		dot.node(root.children[dist].name)
		dot.edge(root.name, root.children[dist].name, str(dist))
		tree_vis(root.children[dist], dot)
	# print(dot.source)
	return dot.render(directory='doctest-output2', view=True)




# From words
# with open("words", "rb") as fp:   # Unpickling
# 	words = pickle.load(fp)
#
# main_root = build_tree(words[:10])
# create_vis(main_root)




# From nodes
with open("nodes", "rb") as fp:
	nodes = pickle.load(fp)
main_root = nodes[0]
create_vis(main_root)




# a= dot.node('help')
# b = dot.node('hell')
# dot.edge('help', 'hell', '1')
# dot.edges(['AB', 'AC', 'AD', 'BE', 'CF', 'CG', 'DH'])
# print(dot.source)
# print(dot.render(directory='doctest-output', view=True))







