from math import dist


def print_tree(root):
    """
    print tree structure in breadth first search order

    :param root: root node of the tree
    :return: None
    """

    # use a queue to store nodes in current level
    queue = [root]

    # loop until the queue is empty
    while len(queue) > 0:

        # get the first node in the queue
        node = queue.pop(0)

        # if it has a left child, append it to the queue
        if node.left is not None:
            queue.append(node.left)

        # if it has a right child, append it to the queue
        if node.right is not None:
            queue.append(node.right)

        # print the value of current node
        print(node)

# ------------------


def pathToNode(root, path, k):

    # base case handling
    if root is None:
        return False

     # append the node value in path
    path.append(root.val)

    # See if the k is same as root's val
    if root.val == k:
        return True

    # Check if k is found in left or right
    # sub-tree
    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right != None and pathToNode(root.right, path, k))):
        return True

    # If not present in subtree rooted with root,
    # remove root from path and return False
    path.pop()
    return False


def distance(root, data1, data2):
    if root:
        # store path corresponding to node: data1
        path1 = []
        pathToNode(root, path1, data1)

        # store path corresponding to node: data2
        path2 = []
        pathToNode(root, path2, data2)

        # iterate through the paths to find the
        # common path length
        i = 0
        while i < len(path1) and i < len(path2):
            # get out as soon as the path differs
            # or any path's length get exhausted
            if path1[i] != path2[i]:
                break
            i = i+1

        # get the path length by deducting the
        # intersecting path length (or till LCA)
        return (len(path1)+len(path2)-2*i)
    else:
        return 0


# # Driver Code to test above functions
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.right.right = Node(7)
# root.right.left = Node(6)
# root.left.right = Node(5)
# root.right.left.right = Node(8)

# dist = distance(root, 4, 5)
# print("Distance between node {} & {}: {}".format(4, 5, dist))

# dist = distance(root, 4, 6)
# print("Distance between node {} & {}: {}".format(4, 6, dist))

# dist = distance(root, 3, 4)
# print("Distance between node {} & {}: {}".format(3, 4, dist))

# dist = distance(root, 2, 4)
# print("Distance between node {} & {}: {}".format(2, 4, dist))

# dist = distance(root, 8, 5)
# print("Distance between node {} & {}: {}".format(8, 5, dist))

# # This program is contributed by Aartee
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def construct_tree(adj_list):
    """
    construct a tree based on a given adjacency list

    :param adj_list: a list of lists, each sublist is an edge in the tree, the first element is the parent node, the second element is the child node
    :return: root node of the tree
    """

    # create a dictionary to store all nodes in the tree, key is the node value, value is the node object itself
    nodes = {}

    # create all nodes in the tree and put them into nodes dictionary
    for edge in adj_list:
        if edge[0] not in nodes:  # if parent node not in dictionary, create one and put it into dictionary
            nodes[edge[0]] = Node(edge[0])

        if edge[1] not in nodes:  # if child node not in dictionary, create one and put it into dictionary
            nodes[edge[1]] = Node(edge[1])

    # construct tree based on adjacency list
    for edge in adj_list:
        parent = nodes[edge[0]]
        child = nodes[edge[1]]

        if parent.left is None:  # if the parent node doesn't have a left child, set the child as the left child
            parent.left = child
        else:  # if the parent node already has a left child, set the child as the right child
            parent.right = child

    # return root node of the tree
    return nodes[adj_list[0][0]]

# adj_list = {0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [1]}

# print_tree(root)

# {
#   (from, to): dist
# }


def solution(n, edges):
    root = construct_tree(edges)
    print(distance(root, 2, 0), distance(root, 0, 1),
          distance(root, 2, 1), "asdasdds")
    cnt = 0
    visited = {}
    sorted_edges = sorted(edges)
    if is_bitree(sorted_edges):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    if distance(root, i, j) + distance(root, j, k) == distance(root, i, k):
                        print(i, j, k)
                        cnt += 1
    else:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if not (i < j < k or i > j > k):
                        continue
                    if i == j or j == k or i == k:
                        continue
                    # if distance(root, i, j) > distance(root, j, k):
                    #     continue
                    if distance(root, i, j) + distance(root, j, k) == distance(root, i, k):
                        print(i, j, k)
                        cnt += 1
    return cnt


def is_bitree(edges):
    for i in range(len(edges)-1):
        if edges[i][1] != edges[i+1][0]:
            return True
    return False


n = 5
edges = [[0, 1], [0, 2], [1, 3], [1, 4]]

n = 4
edges = [[2, 3], [0, 1], [1, 2]]
res = solution(n, edges)

print(res)





# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# def construct_tree(adj_list):
#     # create a dictionary to store all nodes in the tree, key is the node value, value is the node object itself
#     nodes = {}

#     # create all nodes in the tree and put them into nodes dictionary
#     for edge in adj_list:
#         if edge[0] not in nodes:  # if parent node not in dictionary, create one and put it into dictionary
#             nodes[edge[0]] = Node(edge[0])

#         if edge[1] not in nodes:  # if child node not in dictionary, create one and put it into dictionary
#             nodes[edge[1]] = Node(edge[1])

#     # construct tree based on adjacency list
#     for edge in adj_list:
#         parent = nodes[edge[0]]
#         child = nodes[edge[1]]

#         if parent.left is None:  # if the parent node doesn't have a left child, set the child as the left child
#             parent.left = child
#         else:  # if the parent node already has a left child, set the child as the right child
#             parent.right = child

#     # return root node of the tree
#     return nodes[adj_list[0][0]]

# def pathToNode(root, path, k):

#     # base case handling
#     if root is None:
#         return False

#      # append the node value in path
#     path.append(root.val)

#     # See if the k is same as root's val
#     if root.val == k:
#         return True

#     # Check if k is found in left or right
#     # sub-tree
#     if ((root.left != None and pathToNode(root.left, path, k)) or
#             (root.right != None and pathToNode(root.right, path, k))):
#         return True

#     # If not present in subtree rooted with root,
#     # remove root from path and return False
#     path.pop()
#     return False


# def distance(root, data1, data2, visited):
#     if (data1, data2) in visited:
#         return visited[(data1, data2)]
#     if root:
#         # store path corresponding to node: data1
#         path1 = []
#         pathToNode(root, path1, data1)

#         # store path corresponding to node: data2
#         path2 = []
#         pathToNode(root, path2, data2)

#         # iterate through the paths to find the
#         # common path length
#         i = 0
#         while i < len(path1) and i < len(path2):
#             # get out as soon as the path differs
#             # or any path's length get exhausted
#             if path1[i] != path2[i]:
#                 break
#             i = i+1

#         # get the path length by deducting the
#         # intersecting path length (or till LCA)
#         return (len(path1)+len(path2)-2*i)
#     else:
#         return 0

# def is_special_case(edges):
#     for i in range(len(edges)-1):
#         if edges[i][1] != edges[i+1][0]:
#             return True
#     return False

# def solution(n, edges):
#     root = construct_tree(edges)
#     cnt = 0
#     visited = {}
#     sorted_edges = sorted(edges)
#     if is_special_case(sorted_edges):
#         for i in range(n):
#             for j in range(n):
#                 for k in range(n):
#                     if i == j or j == k or i == k:
#                         continue

#                     if (i, j) not in visited:
#                         visited[(i, j)] = distance(root, i, j, visited)
#                     if (j, k) not in visited:
#                         visited[(j, k)] = distance(root, j, k, visited)
#                     if (i, k) not in visited:
#                         visited[(i, k)] = distance(root, i, k, visited)
                    
#                     if visited[(i, j)] + visited[(j, k)] == visited[(i, k)]:
#                         cnt += 1
#     else:
#         for i in range(n):
#             for j in range(n):
#                 for k in range(n):
#                     if not (i < j < k or i > j > k):
#                         continue
#                     if i == j or j == k or i == k:
#                         continue

#                     if (i, j) not in visited:
#                         visited[(i, j)] = distance(root, i, j, visited)
#                     if (j, k) not in visited:
#                         visited[(j, k)] = distance(root, j, k, visited)
#                     if (i, k) not in visited:
#                         visited[(i, k)] = distance(root, i, k, visited)

#                     if visited[(i, j)] + visited[(j, k)] == visited[(i, k)]:
#                         cnt += 1
#     return cnt