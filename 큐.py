import sys
input = sys.stdin.readline


class Queue:
    def __init__(self) -> None:
        self.capacity = 0
        self.arr = []

    def push(self, x):
        self.capacity += 1
        self.arr.append(x)

    def pop(self):
        if self.capacity == 0:
            return -1
        else:
            self.capacity -= 1
            return self.arr.pop(0)
            

    def size(self):
        return self.capacity

    def empty(self):
        return 1 if self.capacity == 0 else 0

    def front(self):
        if self.capacity > 0:
            return self.arr[0]
        else:
            return -1

    def back(self):
        if self.capacity > 0:
            return self.arr[-1]
        else:
            return -1


n = int(input())
q = Queue()

while n:
    n -= 1

    si = list(input().split())
    if len(si) == 2:
        q.push(si[1])
    else:
        if si[0] == 'front':
            print(q.front())
        elif si[0] == 'back':
            print(q.back())
        elif si[0] == 'size':
            print(q.size())
        elif si[0] == 'empty':
            print(q.empty())
        elif si[0] == 'pop':
            print(q.pop())
