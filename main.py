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
        try:
            return node in self._node
        except TypeError:
            return False

    def __len__(self):
        return len(self._node)

    def add_node(self, node_to_add):
        # Null check
        if node_to_add is None:
            raise ValueError("Node cannot be none!")

        # Check if the node already exists
        if node_to_add in self._node.keys():
            raise Exception("Node already in graph!")

        self._adj[node_to_add] = self.adjlist_inner_factory()
        self._node[node_to_add] = self.node_factory()

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
            self._node[v] = self.node_attr_factory()

        # Add the edge
        datadict = self._adj[u].get(v, self.edge_attr_factory())
        datadict.update(attr)  # Allows us to add whatever attributes we want, including weights.
        self._adj[u][v] = datadict
        self._adj[v][u] = datadict

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

    def nodes(self):
        return self._node.items()

    def edges(self):
        return self._adj.items()


def main():
    G = Graph()
    [G.add_node(x) for x in range(5)]
    print(G.nodes())
    print(G.edges())
    print()

    G.add_edge(0, 1, weight=11)
    G.add_edge(1, 2, weight=7)
    G.add_edge(0,2,weight=3)
    print(G.nodes())
    print(G.edges())
    print()

    G.remove_node(1)
    print(G.nodes())
    print(G.edges())


if __name__ == "__main__":
    main()


