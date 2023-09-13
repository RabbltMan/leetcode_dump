from typing import *

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if (grid[0][0]):
            return False
        pos = [None] * (len(grid) ** 2)
        for i, lineList in enumerate(grid):
            for j in range(len(lineList)):
                pos[lineList[j]] = (i, j)

        for i in range(1, len(pos)):
            dx, dy = abs(pos[i][0] - pos[i-1][0]), abs(pos[i][1] - pos[i-1][1])
            if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
                continue
            else:
                return False
        
        return True
    