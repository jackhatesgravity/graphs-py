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

    def remove_node_attr(self, attr):
        for u in self._node:
            if attr in self._node[u]:
                del self._node[u][attr]

    def clear_node_attrs(self):
        for u in self._node:
            self._node[u].clear()

    # Return a list of all attrs. Ugly, needs work.
    # def get_node_attrs(self, node):
    #     print([str(y.keys()) for x,y in self._node.items()])

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


def main():
    G = Graph()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    [G.add_node(alphabet[x], colour="grey") for x in range(5)]

    G.add_edge("a", "b", weight=1)
    G.add_edge("a", "c", weight=3)

    G.nodes["a"]["colour"] = "red"
    print(G.nodes)

if __name__ == "__main__":
    main()


