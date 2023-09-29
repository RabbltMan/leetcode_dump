from bisect import *
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts, ends = sorted([s for s, _ in flowers]), sorted([e for _, e in flowers])
        return [bisect_right(starts, t) - bisect_left(ends, t) for t in people]