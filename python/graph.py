import sys
from collections import deque


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
        self.adj_mat = Graph.adjacency_matrix(self.n, self.vertices, edges)
        self.adj_list = Graph.adjacency_list(self.n, self.vertices, edges)

    def vertices_from_edges(edges: list[Edge] | list[DirectedEdge]) -> list[any]:
        vertices = set()
        for edge in edges:
            vertices.add(edge.src)
            vertices.add(edge.dst)
        return list(sorted(vertices))

    def vertices_mapping(vertices) -> dict[str, int]:
        return {v: i for i, v in enumerate(vertices)}

    def adjacency_matrix(n, vertices, edges) -> list[list[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        mapping = Graph.vertices_mapping(vertices)
        for e in edges:
            i = mapping[e.src]
            j = mapping[e.dst]
            grid[i][j] = e.w
            if not isinstance(edges[0], DirectedEdge):
                j = mapping[e.src]
                i = mapping[e.dst]
                grid[i][j] = e.w
        return grid

    def adjacency_list(n, vertices, edges) -> list[list[int]]:
        grid = [[] for _ in range(n)]
        mapping = Graph.vertices_mapping(vertices)
        for e in edges:
            i = mapping[e.src]
            j = mapping[e.dst]
            grid[i].append(j)
            if isinstance(edges[0], Edge):
                j = mapping[e.src]
                i = mapping[e.dst]
                grid[i].append(j)
        return grid

    def dfs(self, src):
        q = deque()
        q.append(src)
        seen = set()
        while len(q) > 0:
            current = q.pop()
            if current not in seen:
                seen.add(current)
                for w in self.adj_list[current]:
                    q.append(w)

    def dijkstra(self, src, dst):
        dist = [sys.maxsize] * self.n
        dist[src] = 0
        prev = [None] * self.n
        seen = [False] * self.n

        def min_dist():
            m = (None, sys.maxsize)
            for v in enumerate(dist):
                if not seen[v[0]]:
                    m = min(m, v, key=lambda x: x[1])
            return m[0]

        def path():
            p = deque()
            u = dst
            assert prev[u] is not None or u == src, "Target not reachable, or equal to src"

            while u is not None:
                p.appendleft(u)
                u = prev[u]
            return p

        for _ in range(self.n):
            u = min_dist()
            if u == dst or u == None:
                break
            seen[u] = True

            for v in range(self.n):
                if not seen[v] and self.adj_mat[u][v] > 0:
                    alt = dist[u] + self.adj_mat[u][v]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u

        return dist[dst], path()
