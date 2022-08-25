# Olha Svezhentseva
# 24.08.2022

from bk_program.graph_visualisation import create_vis
from bk_program.program import initialize_program, create_tree, show_tree_info, run_interactive_mode

if __name__ == "__main__":
    # words, distance_calc = initialize_program("small_derewo.txt", "edit")
    # Had to change path?
    words, distance_calc = initialize_program("/Users/olhasvezhentseva/pro2-bk-tree/small_derewo.txt", "edit")

    # Using dice coefficient
    # words, distance_calc = initialize_program("small_derewo.txt", "dice")

    reconstructed_tree = create_tree(distance_calc, words)
    create_vis(reconstructed_tree.main_root)
    show_tree_info(reconstructed_tree)
    run_interactive_mode(reconstructed_tree)

