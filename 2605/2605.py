from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        dup = set(nums1) & set(nums2)
        if (dup):
            return min(dup)
        return min(min(nums1) * 10 + min(nums2), min(nums2) * 10 + min(nums1))