from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        currentNode, prevNode = dummy.next, dummy
        while(currentNode and (postNode := currentNode.next)):
            prevNode.next = currentNode.next
            currentNode.next = postNode.next
            postNode.next = currentNode
            prevNode = prevNode.next.next
            currentNode = currentNode.next

        return dummy.next
        