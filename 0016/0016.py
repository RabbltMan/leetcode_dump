from math import *
from typing import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = inf
        n = len(nums)

        for i in range(n-2):
            x = nums[i]
            if (i > 0 and x == nums[i-1]):
                continue
            if ((minSum := x + nums[i+1] + nums[i+2]) > target):
                return minSum if abs(minSum - target) < abs(res - target) else res 
            if ((maxSum := x + nums[n-1] + nums[n-2]) < target):
                res = maxSum if abs(maxSum - target) < abs(res - target) else res
                continue
            j, k = i + 1, n - 1

            while (j < k):
                s = x + nums[j] + nums[k]
                if abs(distance := s - target) < abs(res - target):
                    res = s
                    if distance == 0:
                        return res
                if distance < 0:
                    j += 1
                    while (j < k and nums[j] == nums[j-1]):
                        j += 1
                else:
                    k -= 1
                    while (j < k and nums[k] == nums[k+1]):
                        k -= 1

        return res
        