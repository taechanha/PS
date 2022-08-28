class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
root = Node()
tmp = root

n = int(input())
for _ in range(n):
    a, b, c = input().split()
    tmp.data = a
    if b != '.':
        tmp.left = Node(b)
    if c != '.':
        tmp.right = Node(c)
        
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .