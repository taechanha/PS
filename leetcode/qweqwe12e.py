import itertools


def _combinations_knoothe(n, r):
    global imap

    def y2x(y):
        return tuple(yy + i for i, yy in enumerate(y))
    return map(y2x, itertools.combinations(range(1, n-r+1+1), r))


def combinations_knoothe(seq, r):
    return _combinations_knoothe(len(seq), r)


def solution(n):
    global imap
    imap = lambda *args, **kwargs: list(map(*args, **kwargs))
    return list(combinations_knoothe(range(1, n+1), 1))


res = solution(1)
print(res)




from threading import Semaphore

class Foo:
    def __init__(self):
        self.sem1 = Semaphore(0)
        self.sem2 = Semaphore(0)

    def we(self) -> None:
        print('we', end='')
        self.sem1.release()

    def never(self) -> None:
        self.sem1.acquire()
        print('never', end='')
        self.sem2.release()

    def giveup(self) -> None:
        self.sem2.acquire()
        print('giveup', end='')
        self.sem2.release()
        
        
###################
# 수정하지 말아주세요! #
###################
import sys
import threading
for line in sys.stdin:
    methods = eval(line)
    break
f = Foo()
threads = []
for m in methods:    
    threads.append(threading.Thread(target=getattr(f, m)))
for t in threads:
    t.start()
for t in threads:
    t.join()
