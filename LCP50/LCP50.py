from typing import *

class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for a, b in operations:
            trans = gem[a] // 2
            gem[a] -= trans
            gem[b] += trans

        return max(gem) - min(gem)
