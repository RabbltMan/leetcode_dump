from typing import *

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        maxHeight = max(height)

        while(left < right):
            if (area >= maxHeight * (right - left)):
                return area
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            

        return area
