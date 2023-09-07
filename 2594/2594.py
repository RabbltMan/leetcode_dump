from typing import List
from math import *

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        leftBound, rightBound = 1, ranks[0] * cars * cars
        while (leftBound < rightBound):
            time = (leftBound + rightBound) // 2
            repairCount = 0
            for rank in ranks:
                repairCount += floor((time / rank) ** 0.5)
            if repairCount >= cars:
                rightBound = time
            else:
                leftBound = time + 1

        return leftBound