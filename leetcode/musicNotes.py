
# N Q
# 3 5
# 2
# 1
# 3
# 2
# 3
# 4
# 0
# 1

# import sys
# read = sys.stdin.readline


# def set_song(B):
#     # set beat by duration B
#     song = {}
#     for note, duration in enumerate(B):
#         song[note+1] = duration

#     return song


# def query(song, t):
#     accum = 0

#     for k in range(1, len(song) + 1):
#         accum += song[k]
#         if t < accum:
#             return k


# def main():
#     N, Q = map(int, read().split())
#     B = []
#     T = []
#     for _ in range(N):
#         B.append(int(read()))
#     for _ in range(Q):
#         T.append(int(read()))

#     song = set_song(B)
#     for t in T:
#         print(query(song, t))


# if __name__ == '__main__':
#     main()


# now = 0
# notes = []
# N, Q = map(int, input().split())
# for i in range(1, N + 1):
#     count = int(input())
#     notes.append(now + count - 1)
#     now += count
#     print(now)
# print()
# print(notes)

# [1,2,5], 3
import sys
import bisect

read = sys.stdin.readline
N, Q = map(int, read().split())
song = []
curr = 0
for _ in range(N):
    duration = int(read())
    song.append(curr + duration - 1)
    curr += duration

for _ in range(Q):
    q = int(read())
    print(bisect.bisect_left(song, q) + 1)


def bisect_left(a, x, lo=0, hi=None, *, key=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(i, x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
