from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        ans = [i for i in range(2, n+1)]
        nextFriend, step = 1, 1
        while True:
            nextFriend = (nextFriend + step * k) % n
            if (nextFriend == 0):
                nextFriend = n
            if (nextFriend not in ans):
                return ans
            else:
                ans.pop(ans.index(nextFriend))
                step += 1