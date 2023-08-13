from typing import *
# from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        i = 0
        stack, ans = [], []
        while (head.next != None):
            ans.append(0)
            while(stack):
                if (stack[-1][0] < head.val):
                    ans[stack.pop()[1]] = head.val
                else:
                    break
            stack.append((head.val, i))
            head = head.next
            i += 1
        ans.append(0)
        while(stack):
            if (stack[-1][0] < head.val):
                ans[stack.pop()[1]] = head.val
            else:
                break
        return ans
    
a = Solution()
listNodeTest = ListNode(2, ListNode(1, ListNode(5)))
print(a.nextLargerNodes(listNodeTest))