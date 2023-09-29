from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 1
        for state in flowerbed:
            if state == 0:
                cnt += 1
            else:
                cnt = 0
            if cnt == 3:
                n -= 1
                cnt = 1
            if n == 0:
                return True
                
        return True if n == 1 and cnt == 2 else False