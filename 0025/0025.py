from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        currentNode, leftEdge = head, dummy
        nodeNum = 0
        while(currentNode):
            nodeNum += 1
            currentNode = currentNode.next
        prevNode, currentNode = None, head
        while (nodeNum >= k):
            nodeNum -= k
            for _ in range(k):
                nextNode = currentNode.next
                currentNode.next = prevNode
                prevNode = currentNode
                currentNode = nextNode
            nextNode = leftEdge.next
            nextNode.next = currentNode
            leftEdge.next = prevNode
            leftEdge = nextNode

        return dummy.next
