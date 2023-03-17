from typing import *
class Solution:
    def binarySearch(self, series, num):
        if (len(series) == 1):
            return series[0]
        halfIndex = (len(series) - 1) // 2
        if (num == series[halfIndex]):
            return num
        elif (num < series[halfIndex]):
            if (num < series[halfIndex -1]):
                return self.binarySearch(series[0: halfIndex], num)
            else:
                return series[halfIndex - 1]
        else:
            if (num > series[halfIndex + 1]):
                return self.binarySearch(series[halfIndex + 1: ], num)
            else:
                return series[halfIndex]
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        preSum = [nums[0]]
        res = []
        for i in range(1, len(nums)):
            preSum.append(preSum[i-1] + nums[i])
        for i in range(len(queries)):
            if (queries[i] < nums[0]):
                res.append(0)
            elif (queries[i] == nums[0]):
                res.append(1)
            elif (queries[i] >= preSum[-1]):
                res.append(len(nums))
            else:
                lastSubElement = preSum.index(self.binarySearch(preSum, queries[i])) + 1
                res.append(lastSubElement)
        return res