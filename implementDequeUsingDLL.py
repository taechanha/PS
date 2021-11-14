class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k = k
        self.len = 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.len += 1
        self._add(self.head, ListNode(value))

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.len += 1
        self._add(self.tail.left, ListNode(value))

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.len -= 1
        self._del(self.head)

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.len -= 1
        self._del(self.tail.left.left)

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.right.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.left.val

    def isEmpty(self) -> bool:
        return self.head.right == self.tail

    def isFull(self) -> bool:
        return self.len == self.k
