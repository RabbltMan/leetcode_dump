from typing import *
from itertools import *

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        maxResLen, r = 0, target
        for num in candidates:
            r -= num
            if r >= 0:
                maxResLen += 1
            else:
                break
        c = []
        for num, l in groupby(candidates):
            c += [num] * min(maxResLen, len(list(l)))
        candidates = c
        del c, maxResLen, r
        res = []
        def dfs(prev, target, left=0):
            l = candidates[left: ]
            if (sum(l) < target):
                return
            if (sum(l) == target):
                cur = prev.copy()
                cur += l
                if cur not in res:
                    res.append(cur)
                return
            for i, num in enumerate(l):
                cur = prev.copy()
                if num == target:
                    cur.append(num)
                    if cur not in res:
                        res.append(cur)
                elif num > target:
                    return
                else:
                    cur.append(num)
                    dfs(cur, target-num, left + i + 1)
        dfs([], target)

        return res
