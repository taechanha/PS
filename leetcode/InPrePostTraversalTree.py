class Tree:
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right


def in_order_traverse(node):
    if node == None:
        return
    else:
        in_order_traverse(node.left)
        print(node.val)
        in_order_traverse(node.right)


def pre_order_traverse(node):
    if node == None:
        return
    else:
        print(node.val)
        pre_order_traverse(node.left)
        pre_order_traverse(node.right)


def post_order_traverse(node):
    if node == None:
        return
    else:
        post_order_traverse(node.left)
        post_order_traverse(node.right)
        print(node.val)


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)
root.left.left.left = Tree(8)
root.left.left.right = Tree(9)

# in_order_traverse(root)
# pre_order_traverse(root)
post_order_traverse(root)
