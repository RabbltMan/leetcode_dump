from typing import *
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        # zeroStats = Counter()
        repeat = 0
        for num in nums:
            if num == 0:
                repeat += 1
                # zeroStats[repeat] += 1
                res += repeat
            else:
                repeat = 0
                # for i in range(2, len(zeroStats) + 1):
                #     zeroStats[i] += zeroStats[i-1]
                # res += sum(zeroStats.values())
                # zeroStats = Counter()
        # for i in range(2, len(zeroStats) + 1):
        #     zeroStats[i] += zeroStats[i-1]
        # res += sum(zeroStats.values())
        return res


a = Solution()
print(a.zeroFilledSubarray([0,0,0,0,0,1,0,0]))