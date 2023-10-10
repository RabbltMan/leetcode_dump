from typing import List

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        nums = [num + d if s[i] == 'R' else num - d for i, num in enumerate(nums)]
        nums.sort()
        res, n = 0, len(nums)
        for i in range(1, n):
            res += i * (n - i) * (nums[i] - nums[i-1])

        return res % 1_000_000_007