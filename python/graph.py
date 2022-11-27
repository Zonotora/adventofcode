import sys
import numpy as np


class Edge:
    def __init__(self, src, dst, w) -> None:
        self.src = src
        self.dst = dst
        self.w = w

    def __repr__(self) -> str:
        return f"<{self.src} -> {self.dst}, {self.w}>"


class DirectedEdge(Edge):
    pass


class Graph:
    def __init__(self, edges: list[Edge] | list[DirectedEdge]):
        assert isinstance(edges, list)
        assert len(edges) > 0
        assert isinstance(edges[0], Edge) or isinstance(edges[0], DirectedEdge)
        self.edges = edges
        self.vertices = Graph.vertices_from_edges(edges)
        self.n = len(self.vertices)
        self.adj = Graph.adjacency(self.n, self.vertices, edges)

    def vertices_from_edges(edges: list[Edge] | list[DirectedEdge]) -> list[any]:
        vertices = set()
        for edge in edges:
            vertices.add(edge.src)
            vertices.add(edge.dst)
        return list(sorted(vertices))

    def adjacency(n, vertices, edges) -> list[list[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        mapping = {v: i for i, v in enumerate(vertices)}
        for e in edges:
            i = mapping[e.src]
            j = mapping[e.dst]
            grid[i][j] = e.w
            if isinstance(edges[0], Edge):
                j = mapping[e.src]
                i = mapping[e.dst]
                grid[i][j] = e.w
        return grid
