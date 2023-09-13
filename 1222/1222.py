from typing import *

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def search(direction: Literal[0, 1, 2, 3, 4, 5, 6, 7]):
            x, y = king
            dx, dy = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))[direction]
            while (0 <= x < 8 and 0 <= y < 8):
                x += dx
                y += dy
                if [x, y] in queens:
                    res.append([x, y])
                    return
        res = []
        for i in range(8):
            search(i)

        return res
