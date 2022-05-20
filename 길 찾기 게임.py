###############
##매우 좋은 문제##
###############

# **프로그래머스에서 sys.setrecursionlimit(SOME NUMBER) 안 주면 런타임 에러나는디 다른 사람은 어떻게 해결했나?


# 문제: 좌표로 부터 이진 트리 구성

# 좌표: [x, y] -> [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

# [1] 트리 구성
# *완전 이진 트리가 보장되어 있지 않음. 따라서
# 0. preprocess: 먼저 y 값이 큰 순서로 정렬,
# 1. 맨 위 노드(root)를 고른 후, 칸 수 상관없이 바로 아래에 있는 노드를 두 개 고름.
# 2. 그 중 x 값이 root.x 보다 작은 놈을 root.left로, 큰 놈을 root.right로 (같은 경우는 불가능)

# [2] 전위, 후위 순회

R, C, K = map(int, input().split())

class Node:
    def __init__(self, x, y, data, left=None, right=None):
        self.left = left
        self.right = right
        self.x = x
        self.y = y
        self.data = data

def solution(nodeinfo):
    global coord2idx

    coord2idx = dict()
    for i, node in enumerate(nodeinfo):
        coord2idx[str(node)] = i+1

    nodeinfo.sort(key=lambda x: [-x[1], x[0]])

    node = nodeinfo[0]
    # root: [None, None, 5, 3, "[5,3]"]
    root = Node(x=node[0], y=node[1], data=coord2idx[str(node)])

    for i, node in enumerate(nodeinfo[1:]):
        # [[3, 5], [11, 5], ... ] | node: [3, 5]
        construct_btree(root, node)

    global preorder_data, postorder_data
    preorder_data, postorder_data = [], []
    preorder_traversal(root)
    postorder_traversal(root)

    return [preorder_data, postorder_data]


def construct_btree(base_node: Node, node: list[int]):

    if base_node.x > node[0] and base_node.y > node[1]:
        if base_node.left == None:
            chosen_node = Node(x=node[0], y=node[1], data=coord2idx[str(node)])
            base_node.left = chosen_node
            return
        construct_btree(base_node.left, node)

    elif base_node.x < node[0] and base_node.y > node[1]:
        if base_node.right == None:
            chosen_node = Node(x=node[0], y=node[1], data=coord2idx[str(node)])
            base_node.right = chosen_node
            return
        construct_btree(base_node.right, node)

# left -> right -> parent


def preorder_traversal(node: Node):
    if node == None:
        return
    preorder_data.append(node.data)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

# right -> left -> parent


def postorder_traversal(node: Node):
    if node == None:
        return
    postorder_traversal(node.left)  # 다시 따라가보기
    postorder_traversal(node.right)
    postorder_data.append(node.data)


##

nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5],
            [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
res = solution(nodeinfo)

print(res)
