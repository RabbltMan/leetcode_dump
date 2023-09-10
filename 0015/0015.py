from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n-2):
            x = nums[i]
            if (i > 0 and x == nums[i-1]):
                continue
            j, k = i + 1, n - 1

            if (x + nums[j] + nums[j+1] > 0):
                break
            
            if (x + nums[k] + nums[k-1] < 0):
                continue

            while (j < k):
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while (j < k and nums[j] == nums[j-1]):
                        j += 1
                    k -= 1
                    while (j < k and nums[k] == nums[k+1]):
                        k -= 1
        
        return ans
        