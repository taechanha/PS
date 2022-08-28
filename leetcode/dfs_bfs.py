from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, s):
        visited = list()
        stack = list()

        stack.append(s)

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(self.graph[node])

        return visited

    def BFS(self, s):
        visited = list()
        queue = list()
        queue.append(s)

        while queue:
            node = queue.pop(0)
            if node not in visited:
                #print(node, end=" ")
                visited.append(node)
                queue.extend(self.graph[node])

        return visited


g = Graph()
n, m, v = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    g.addEdge(a, b)

print(g.DFS(v))
print(g.BFS(v))
