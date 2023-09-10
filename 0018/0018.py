from typing import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n-3):
            x = nums[i]
            if (i > 0 and x == nums[i-1]):
                continue
            if (x + nums[i+1] + nums[i+2] + nums[i+3] > target):
                break
            if (x + nums[n-1] + nums[n-2] + nums[n-3] < target):
                continue
            for j in range(i+1, n-2):
                y = nums[j]
                if (j > i + 1 and y == nums[j-1]):
                    continue
                if (x + y + nums[n-1] + nums[n-2] < target):
                    continue
                if (x + y + nums[j+1] + nums[j+2] > target):
                    break
                k, l = j + 1, n - 1

                while(k < l):
                    s = x + y + nums[k] + nums[l]
                    if s > target:
                        l -= 1
                    elif s < target:
                        k += 1
                    else:
                        res.append([x, y, nums[k], nums[l]])
                        k += 1
                        while (k < l and nums[k] == nums[k-1]):
                            k += 1
                        l -= 1
                        while (k < l and nums[l] == nums[l+1]):
                            l -= 1
        return res
