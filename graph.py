import math
from typing import Union, TypedDict, TypeAlias, List, Dict

from queue import Queue


class Attribute(TypedDict):
    name: str
    value: Union[str, int, float]


Node: TypeAlias = str
Path: TypeAlias = List[str]


class Graph:
    node_attr_factory = dict
    adjlist_outer_factory = dict
    adjlist_inner_factory = dict
    edge_attr_factory = dict

    def __init__(self) -> None:
        self._node = self.node_attr_factory()  # Captures node attributes
        self._adj = self.adjlist_outer_factory()  # Captures outer adjacency list

    def add_node(self, node_to_add: Node, **attr: Attribute) -> None:
        # Null check
        if node_to_add is None:
            raise ValueError("Node cannot be none!")

        # Check if the node already exists
        if node_to_add not in self._node.keys():
            self._adj[node_to_add] = self.adjlist_inner_factory()
            attr_dict = self._node[node_to_add] = self.node_attr_factory()
            attr_dict.update(attr)
        else:
            self._node[node_to_add].update(attr)

    def remove_node(self, node_to_remove: Node) -> None:
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
    def add_edge(self, u: Node, v: Node, **attr: Attribute) -> None:
        # Add the nodes
        if u not in self._node:
            if u is None:
                raise ValueError("Node cannot be none!")
            self._adj[u] = self.adjlist_inner_factory()
            self._node[u] = self.node_attr_factory()
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

    def remove_edge(self, u: str, v: str) -> None:
        if self._adj[u][v] is not None:
            del self._adj[u][v]
        if u != v:
            del self._adj[v][u]
        else:
            raise Exception("Edge is not in the graph!")

    def has_node(self, node_to_find: Node) -> bool:
        return node_to_find in self._node

    # I could probably add an "has_edge" method here...

    def set_node_attr(self, node: Node, **attr: Attribute) -> None:
        if node not in self._node:
            raise Exception("Node not in graph!")
        self._node[node].update(attr)

    def remove_node_attr(self, **attr: Attribute) -> None:
        for u in self._node:
            if attr in self._node[u]:
                del self._node[u][attr]

    def clear_node_attrs(self) -> None:
        for u in self._node:
            self._node[u].clear()

    def remove_edge_attr(self, attr_name: str) -> None:
        for u in self._adj:
            for v in self._adj[u]:
                if attr_name in self._adj[u][v]:
                    del self._adj[u][v][attr_name]

    def clear_edge_attrs(self) -> None:
        for u in self._adj:
            for v in self._adj[u]:
                self._adj[u][v].clear()

    # Can we be more specific with the return type of these properties?
    @property
    def nodes(self) -> Dict:
        return self._node

    @property
    def edges(self) -> Dict:
        return self._adj


# Typedefs for all of these attrs are cooked. Need to wrap my head around it better.
def breadth_first_search(graph: Graph, source: Node, sink: Node) -> Path:
    # Reset the node attributes to prime the search.
    for key, value in graph.nodes.items():
        graph.set_node_attr(key, colour="white")
        graph.set_node_attr(key, d=math.inf)
        graph.set_node_attr(key, pi=None)

    # Set the attributes for the source node.
    graph.set_node_attr(source, colour="grey")
    graph.set_node_attr(source, d=0)
    graph.set_node_attr(source, pi=None)

    # Create frontier and push source node onto it.
    frontier = Queue()
    frontier.put(source)

    # Perform the search.
    while not frontier.empty():
        u = frontier.get()
        neighbours = graph.edges[u]
        for neighbour in neighbours:
            n = neighbour
            if graph.nodes[n]["colour"] == "white":
                graph.nodes[n]["colour"] = "grey"
                graph.nodes[n]["d"] = graph.nodes[u]["d"] + 1
                graph.nodes[n]["pi"] = u
                frontier.put(n)
        graph.nodes[u]["colour"] = "black"

    path = []
    reconstruct_path(graph, source, sink, path)
    return path


def reconstruct_path(graph: Graph, source: Node, sink: Node, path: Path):
    if sink == source:
        path.append(source)
    elif graph.nodes[sink]["pi"] is None:
        print("No path found!")
    else:
        reconstruct_path(graph, source, graph.nodes[sink]["pi"], path)
        path.append(sink)
