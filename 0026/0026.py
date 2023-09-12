from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, currentNum = 0, 0, None
        for j in range(len(nums)):
            if nums[j] != currentNum:
                nums[i] = nums[j]
                currentNum = nums[i]
                i += 1

        return i
