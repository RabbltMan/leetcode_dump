from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = leftEdge = ListNode(next=head)
        for _ in range(left-1):
            leftEdge = leftEdge.next

        prevNode, currentNode = None, leftEdge.next

        for _ in range(right - left + 1):
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode

        leftEdge.next.next = currentNode
        leftEdge.next = prevNode

        return dummy.next