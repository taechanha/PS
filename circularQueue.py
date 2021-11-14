class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.start = 0
        self.end = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q[self.end] = value
        self.end = (self.end + 1) % self.k

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.q[self.start] = None
        self.start = (self.start + 1) % self.k

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.end]

    def isEmpty(self) -> bool:
        return self.start == self.end and self.q[self.start] is None

    def isFull(self) -> bool:
        return self.start == self.end and self.q[self.start] is not None


# Your MyCircularQueue object will be instantiated and called as such:
myCircularQueue = MyCircularQueue(3)
myCircularQueue.enQueue(1)
myCircularQueue.enQueue(2)
myCircularQueue.enQueue(3)
myCircularQueue.enQueue(4)
myCircularQueue.Rear()
myCircularQueue.isFull()
myCircularQueue.deQueue()
myCircularQueue.enQueue(4)
myCircularQueue.Rear()
# myCircularQueue.Front()
# myCircularQueue.isEmpty()
