from typing import *


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        subNum = len(l)
        res = [False] * subNum
        for i in range(subNum):
            sub = sorted([num for num in nums[l[i]: r[i] + 1]])
            delta = set([(sub[i] - sub[i-1]) for i in range(1, len(sub))])
            if len(delta) == 1:
                res[i] = True
        return res


a = Solution()
print(a.checkArithmeticSubarrays([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]))
