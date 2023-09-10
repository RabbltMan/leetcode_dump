from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        left, right, distance = dummy, dummy, 0
        while (right.next):
            prev = left
            if (distance == n - 1):
                left = left.next
            else:
                distance += 1    
            right = right.next

        prev.next = prev.next.next

        return dummy.next