# Olha Svezhentseva
# 16.08.2022

import graphviz

from .tree import Tree
from .node import Node


class Visualisation:

	def create_vis(self, tree: Tree, graphics: bool, output_dir: str = 'doctest-output') -> None:
		"""
		The method creates a visualisation of a BK-tree.
		Visualisation is saved as a PNG file to output_dir.
		"""
		dot = graphviz.Digraph('BK-tree')
		dot.format = 'png'
		dot.node(tree.main_root.name)
		self._tree_vis(tree.main_root, dot)
		# dot.render(directory=output_dir, view=True)
		if graphics:
			dot.render(directory=output_dir, view=True)
		else:
			dot.save(filename=f'{output_dir}/dot.source')

	def _tree_vis(self, root: Node, dot: graphviz.Digraph) -> None:
		"""The method recursively processes children of main root to create a visualisation of a BK-tree."""
		for dist in root.children:
			dot.node(root.children[dist].name)
			dot.edge(root.name, root.children[dist].name, str(dist))
			self._tree_vis(root.children[dist], dot)
