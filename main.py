# Olha Svezhentseva
# 24.08.2022

import argparse

import bk_program


def show_tree_info(tree: bk_program.Tree, metric: str) -> None:
    """The method prints information about a given tree."""
    print(f"----The tree has been built. -----")
    print(f"It is based on {metric} distance. "
          f"All the subnodes on the edge numbered n have {metric} distance of n to the parent node.")
    print(f'Number of nodes: {tree.get_number_nodes(tree.main_root)}')
    print(f'Tree height: {tree.get_tree_height(tree.main_root)}')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    parser.add_argument("--metric",  nargs='?', default="edit")
    args = parser.parse_args()

    bksearcher = bk_program.BKSearcher(args.file, args.metric)
    show_tree_info(bksearcher.tree, args.metric)

    # Visualisation
    vis = bk_program.Visualisation()
    vis.create_vis(bksearcher.tree,  bksearcher.vis_required)

    # Chat
    chat = bk_program.Chat(bksearcher)
    chat.run_interactive_mode()
