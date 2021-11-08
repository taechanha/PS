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


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    odd = head
    even_head = even = head.next

    while odd and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = even_head
    return head


test_cases = [
    [1, 2, 3, 4, 5]
]

for case in test_cases:
    head = lst2link(case)
    printll(oddEvenList(head))
