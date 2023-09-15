from typing import *
from itertools import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if (len(row) - row.count('.') + 1 != len(set(row))):
                return False
        for block in (product(a, b) for a, b in (product(((0, 1, 2), (3, 4, 5), (6, 7, 8)), repeat=2))):
            block = [board[i][j] for i, j in block]
            if (len(block) - block.count('.') + 1 != len(set(block))):
                return False
        for col in map(list, zip(*board)):
            if (len(col) - col.count('.') + 1 != len(set(col))):
                return False

        return True
