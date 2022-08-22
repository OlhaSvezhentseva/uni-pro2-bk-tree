import pickle
import graphviz



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




# Create visualisation from words
# with open("words", "rb") as fp:   # Unpickling
# 	words = pickle.load(fp)
#
# main_root = build_tree(words[:10])
# create_vis(main_root)




# Create visualisation from pickle file, that contains main root
# with open("main_root", "rb") as fp:
# 	content = pickle.load(fp)
# main_root = content
# create_vis(main_root)
