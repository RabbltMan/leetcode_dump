from typing import *
from itertools import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyTable = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': 'pqrs',
            '8': ('t', 'u', 'v'),
            '9': 'wxyz'
        }

        ans = [''.join(t) for t in product(*(keyTable[d] for d in digits))]
        return ans if digits else []
