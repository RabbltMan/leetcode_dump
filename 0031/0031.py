from typing import *

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, leftNum = None, None
        for i in range(-1, -len(nums), -1):
            if nums[i] > nums[i-1]:
                left, leftNum = i - 1, nums[i-1]
                break        
        if left == None:
            nums.sort()
        else:
            for i in range(-1, left, -1):
                if nums[i] > leftNum:
                    nums[i], nums[left] = nums[left], nums[i]
                    break
            for i in range(1, (-1 - left) // 2 + 1):
                nums[-i], nums[left+i] = nums[left+i], nums[-i]
