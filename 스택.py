import sys
input = sys.stdin.readline

class Stack:
    def __init__(self) -> None:
        self.top = 0
        self.arr = []

    def push(self, x):
        self.arr.append(x)
        self.top += 1

    def pop(self):
        if self.top == 0:
            return -1
        self.top -= 1
        return self.arr.pop()

    def size(self):
        return self.top

    def empty(self):
        return 1 if self.top == 0 else 0

    def peek(self):
        if self.top == 0:
            return -1
        return self.arr[self.top - 1]


t = int(input())
s = Stack()
while t:
    t -= 1
    si = list(map(str, input().split()))
    if len(si) == 1:
        if si[0] == 'pop':
            # test += str(s.pop())
            print(s.pop())
        elif si[0] == 'size':
            # test += str(s.size())
            print(s.size())
        elif si[0] == 'empty':
            # test += str(s.empty())
            print(s.empty())
        else:
            # test += str(s.peek())
            print(s.peek())
    else:
        s.push(si[1])
