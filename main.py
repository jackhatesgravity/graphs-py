from graph import Graph, breadth_first_search, depth_first_search


def main():
    G = Graph()
    graph_nodes = "rstuvwxyz"  # From CLRS, s is source.
    [G.add_node(graph_nodes[x]) for x in range(len(graph_nodes))]

    # This is not efficient, but it's what we've got.
    G.add_edge("s", "r")
    G.add_edge("s", "v")
    G.add_edge("s", "u")
    G.add_edge("t", "r")
    G.add_edge("t", "u")
    G.add_edge("y", "u")
    G.add_edge("y", "v")
    G.add_edge("y", "x")
    G.add_edge("w", "r")
    G.add_edge("w", "v")
    G.add_edge("w", "x")
    G.add_edge("w", "z")
    G.add_edge("x", "z")

    path = breadth_first_search(G, "s", "z")
    print(f"BFS: {path}")
    path.clear()

    path = depth_first_search(G, "s", "z")
    print(f"DFS: {path}")


if __name__ == "__main__":
    main()
