import math

from queue import Queue


class Graph:
    node_factory = dict
    adjlist_outer_factory = dict
    adjlist_inner_factory = dict
    edge_attr_factory = dict

    def __init__(self):
        self._node = self.node_factory()  # Captures node attributes
        self._adj = self.adjlist_outer_factory()  # Captures outer adjacency list

    def __iter__(self):
        return iter(self._node)

    def __contains__(self, node):
        return node in self._node

    def __len__(self):
        return len(self._node)

    def add_node(self, node_to_add, **attr):
        # Null check
        if node_to_add is None:
            raise ValueError("Node cannot be none!")

        # Check if the node already exists
        if node_to_add not in self._node.keys():
            self._adj[node_to_add] = self.adjlist_inner_factory()
            attr_dict = self._node[node_to_add] = self.node_factory()
            attr_dict.update(attr)
        else:
            self._node[node_to_add].update(attr)

    def get_node(self, node):
        if node not in self._node:
            raise Exception(f"Node {node} not in graph!")
        return {node: self._node[node]}

    def remove_node(self, node_to_remove):
        # Null check
        if node_to_remove is None:
            raise ValueError("Node cannot be none!")

        # Check if the node already exists
        if node_to_remove not in self._node:
            raise Exception("Node not in graph!")

        # Remove node from the list of nodes
        adj = self._adj
        neighbours = list(adj[node_to_remove])
        del self._node[node_to_remove]

        # Remove node from adjacency lists
        for neighbour in neighbours:
            del adj[neighbour][node_to_remove]
        del adj[node_to_remove]

    # Overwrites existing edges rather than checking for existing ones. Is this what we want?
    def add_edge(self, u, v, **attr):
        # Add the nodes
        if u not in self._node:
            if u is None:
                raise ValueError("Node cannot be none!")
            self._adj[u] = self.adjlist_inner_factory()
            self._node[u] = self.node_factory()
        if v not in self._node:
            if v is None:
                raise ValueError("Node cannot be none!")
            self._adj[v] = self.adjlist_inner_factory()
            self._node[v] = self.node_factory()

        # Add the edge
        datadict = self._adj[u].get(v, self.edge_attr_factory())
        datadict.update(attr)  # Allows us to add whatever attributes we want, including weights.
        self._adj[u][v] = datadict
        self._adj[v][u] = datadict

    def remove_edge(self, u, v):

        if self._adj[u][v] is not None:
            del self._adj[u][v]
        if u != v:
            del self._adj[v][u]
        else:
            raise Exception("Edge is not in the graph!")

    def has_node(self, node_to_find):
        return node_to_find in self._node

    # I could probably add an "has_edge" method here...

    def set_node_attr(self, node, attr, value):
        if node not in self._node:
            raise Exception("Node not in graph!")
        self._node[node].update({attr: value})

    def remove_node_attr(self, attr):
        for u in self._node:
            if attr in self._node[u]:
                del self._node[u][attr]

    def clear_node_attrs(self):
        for u in self._node:
            self._node[u].clear()

    def remove_edge_attr(self, attr):
        for u in self._adj:
            for v in self._adj[u]:
                if attr in self._adj[u][v]:
                    del self._adj[u][v][attr]

    def clear_edge_attrs(self):
        for u in self._adj:
            for v in self._adj[u]:
                self._adj[u][v].clear()

    @property
    def nodes(self):
        return self._node

    @property
    def edges(self):
        return self._adj


def breadth_first_search(G, s):
    # Reset the node attributes to prime the search.
    for key, value in G.nodes.items():
        G.set_node_attr(key, "colour", "white")
        G.set_node_attr(key, "d", math.inf)
        G.set_node_attr(key, "pi", None)

    # Set the attributes for the source node.
    G.set_node_attr(s, "colour", "grey")
    G.set_node_attr(s, "d", 0)
    G.set_node_attr(s, "pi", None)

    # Create frontier and push source node onto it.
    frontier = Queue()
    frontier.put(s)

    # Perform the search.
    while not frontier.empty():
        u = frontier.get()
        neighbours = G.edges[u]
        for neighbour in neighbours:
            n = neighbour
            if G.nodes[n]["colour"] == "white":
                G.nodes[n]["colour"] = "grey"
                G.nodes[n]["d"] = G.nodes[u]["d"] + 1
                G.nodes[n]["pi"] = u
                frontier.put(n)
        G.nodes[u]["colour"] = "black"


def print_path(G, s, t, path):
    if t == s:
        path.append(s)
    elif G.nodes[t]["pi"] is None:
        print("No path found!")
    else:
        print_path(G, s, G.nodes[t]["pi"], path)
        path.append(t)


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

    breadth_first_search(G, "s")

    path = []
    print_path(G, "s", "z", path)
    print(path)
    # print(G.nodes["z"]["pi"])



if __name__ == "__main__":
    main()
