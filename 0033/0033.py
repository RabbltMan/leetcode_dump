from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while(l < r):
            mid = (r + l) // 2
            if nums[l] <= target <= nums[mid] or (nums[l] > nums[mid] and (target <= nums[mid] or target >= nums[l])):
                if target == nums[mid]:
                    return mid
                r = mid
            else:
                l = mid + 1

        return l if l == r and nums[l] == target else -1
