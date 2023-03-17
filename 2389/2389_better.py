from typing import *
from bisect import *
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        for i, val in enumerate(queries):
            queries[i] = bisect_right(nums, val)
        return queries