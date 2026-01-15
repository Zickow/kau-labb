# Zakaria Bouchaoui och Elias Bouchaoui

def show_2d(tree):
    """
    Print the tree in 2D. Empty nodes are shown as '.'.
    Scales with the number of levels and spacing by height.
    """
    levels = tree.bfs_order_star()

    if not levels:
        print("Empty tree")
        return

    h = tree.height()
    index = 0
    level = 0
    num_nodes = 1

    while index < len(levels):
        # Scale spacing: deeper levels get less spacing
        spacing = max(1, 4 - level)
        
        line_nodes = levels[index:index+num_nodes]
        line_str = ""
        for n in line_nodes:
            if n is None:
                line_str += " . ".center(spacing*2)
            else:
                line_str += f"[{n}]".center(spacing*2)
        print(line_str)
        index += num_nodes
        num_nodes *= 2
        level += 1
