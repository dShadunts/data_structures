from queue import Queue


# Implementation of undirected graph using adjacency list
class Vertex:
    def __init__(self, data):
        self.data = data
        self.neighbors = {}

    def add_neighbor(self, v, w=0):
        self.neighbors[v] = w

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, data):
        self.size += 1
        v = Vertex(data)
        self.vertices[data] = v
        return v

    def add_edge(self, src, dest, w=0):
        if src not in self.vertices:
            self.add_vertex(src)
        if dest not in self.vertices:
            self.add_vertex(dest)
        # undirected graph
        self.vertices[src].add_neighbor(self.vertices[dest], w)
        self.vertices[dest].add_neighbor(self.vertices[src], w)

    # Breadth first search algorithm
    def bfs(self, src, goal_test):
        # keep track of visited vertices
        visited = {}
        q = Queue()

        # first visit src node
        q.enqueue(src)
        visited[src.data] = True

        while not q.is_empty():
            # test next node in the queue for goal
            curr = q.dequeue()
            if goal_test(curr):
                return curr
            # add unvisited neighbors to the queue
            for v in curr.get_neighbors():
                if v.data not in visited:
                    q.enqueue(v)
                    visited[v.data] = True

    # Recursive Depth first search algorithm
    def dfs(self, src, goal_test, path=[]):
        # found the goal -> stop
        if goal_test(src, path): return path
        # add current vertex to the path
        path += [src]
        for v in src.get_neighbors():
            # don't visit same vertex twice
            if v not in path:
                path = self.dfs(v, goal_test, path)
        return path

    # Recursively detect if graph has a cycle
    def has_cycle(self, v, parent=None, visited={}):
        # mark current as visited 
        visited[v] = True

        for n in v.get_neighbors():
            # found an unvisited neighbor -> check for cycle
            if not n not in visited:
                if self.has_cycle(n, v, visited):
                    return True
            # if n is visited and is not a parent of current -> there is a cycle
            elif n != parent:
                return True

        return False

    # Check if graph is a tree
    def is_tree(self):
        # empty graph is a tree
        if len(self.vertices.keys()) == 0:
            return True
        # pick a vertex
        src = self.vertices.itervalues().next()
        visited = {}
        # check for a cycle
        is_cyclic = self.has_cycle(src, visited=visited)
        # visited now contains all the vertices reachable from src
        is_connected = len(visited.keys()) == self.size
        # connected and acyclic -> tree
        return is_connected and not is_cyclic

    def num_of_edges(self):
        num = 0
        for v in self:
            num += len(v.get_neighbors())
        # for an undirected graph
        return num / 2

    # Single pare shortest paths from src vertex
    # returns: 
    # 1. cost of shortest path for every vertex
    # 2. dictionary containing actual path
    def dijkstra(self, src):
        inf = float('inf')
        # originally all nodes have infinity distance from the src
        dist = {v: inf for v in self.vertices.values()}
        # and no parents
        parents = {v: None for v in self.vertices.values()}
        # start from src
        dist[src] = 0
        vertices = list(self.vertices.values())
        while vertices:
            # get vertex with closest to the current
            curr = min(vertices, key=lambda v: dist[v])
            # can't relax anything if the minimum distance is infinity
            if dist[curr] == inf:
                break
            for neighbor in curr.get_neighbors():
                # the cost of reaching neighbor through current vertex
                alt = dist[curr] + curr.get_weight(neighbor)
                # found a better path -> relax
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    parents[neighbor] = curr
            vertices.remove(curr)
        return dist, parents
