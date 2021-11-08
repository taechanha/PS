from typing import *
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


def printll(head: Optional[ListNode]):
    while head:
        print(head.val)
        head = head.next


def reverseLinkedList(head: Optional[ListNode], m, n) -> Optional[ListNode]:
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head

    for _ in range(m - 1):
        start = start.next
    end = start.next

    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp

    return root.next


test_cases = [
    [[1, 2, 3, 4, 5, 6], [2, 5]]
]

for case in test_cases:
    head = lst2link(case[0])
    m, n = case[1]
    printll(reverseLinkedList(head, m, n))
