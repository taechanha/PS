class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


class Solution:
    def solve(self, n, m, roads, bases):
        graph = {}
        for i in range(n):
            graph[i] = Node(i)
        for road in roads:
            graph[road[0]].neighbors.append(graph[road[1]])
            graph[road[1]].neighbors.append(graph[road[0]])
        for base in bases:
            graph[base].val = 1
        queue = [graph[bases[0]]]
        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                if neighbor.val == 0:
                    neighbor.val = node.val
                    queue.append(neighbor)
        count = 0
        for node in graph.values():
            if node.val == 1:
                count += 1
        if count > n / 2:
            return [count, -1]
        else:
            return [count, n - count]
