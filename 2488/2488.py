from typing import *
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        s = 0
        counter = Counter()
        counter[0] = 1
        kIndex = nums.index(k)
        result = 0

        for i, num in enumerate(nums):
            if num > k:
                s += 1
            elif num < k:
                s -= 1
            if i < kIndex:
                counter[s] += 1
            else:
                result += counter[s] + counter[s-1]
                
        return result