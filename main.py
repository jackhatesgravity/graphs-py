from typing import Union

Edge = Union[str, int]  # I don't think this is right, but putting it down for now.


class Vertex:
    def __str__(self):
        return f"{self.key}"

    def __init__(self, key):
        self.key = str(key)  # Enforce string type, I think?
        self.neighbours = []  # How do I assign weights to the edges, though?


class Graph:
    """
    Leaning towards making this an adjacency-list representation for a Graph.
    Start by making something a little more basic-bitch, and then tweak as we go.
    """

    # This is uuuuuuuuuugly code. Real ugly. But it works.
    def __str__(self):
        result = ""
        vertices = list(self.vertices)
        for i in range(len(vertices) - 1):
            result += f"{vertices[i]}, "
        result += str(vertices[-1])
        return result

    def __init__(self):
        self.vertices = set()

    def count(self):
        return len(self.vertices)

    def empty(self):
        return self.count == 0

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.add(v)
        else:
            raise Exception("Vertex already exists in Graph!")

    # Removing a vertex needs to take all of its references with it.
    def remove_vertex(self, v):
        if v in self.vertices:
            self.vertices.remove(v)
        else:
            raise Exception("Vertex not found in Graph!")

    # Also, I like the CLRS description of a weight function. Keep it separate.


def main():
    g = Graph()
    v1 = Vertex("v1")
    v2 = Vertex("v2")
    v3 = Vertex("v3")

    verts = [v1, v2, v3]
    for v in verts:
        g.add_vertex(v)
    print(g)

    try:
        g.add_vertex(v1)
    except Exception as e:
        print(e)

    g.remove_vertex(v1)
    print(g)

    try:
        g.remove_vertex(v1)
    except Exception as e:
        print(e)

    g.add_vertex(v1)
    print(g)


if __name__ == "__main__":
    main()
