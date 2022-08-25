# Olha Svezhentseva
# 16.08.2022

import graphviz
from bk_program.node import Node


def create_vis(main_root: Node, output_dir: str = 'doctest-output') -> None:
	"""
	The method creates a visualisation of a BK-tree.
	Visualisation is saved as a PNG file to output_dir.
	"""
	dot = graphviz.Digraph('BK-tree')
	dot.format = 'png'
	dot.node(main_root.name)
	_tree_vis(main_root, dot)
	dot.render(directory=output_dir, view=True)


def _tree_vis(root: Node, dot: graphviz.Digraph) -> None:
	"""
	The method recursively processes children of main root to create a visualisation of a BK-tree.
	"""
	for dist in root.children:
		dot.node(root.children[dist].name)
		dot.edge(root.name, root.children[dist].name, str(dist))
		_tree_vis(root.children[dist], dot)
