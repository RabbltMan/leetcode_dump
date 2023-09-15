from typing import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(prev: List, target: int, left=0):
            for i, num in enumerate(candidates[left:]):
                if target - num == 0:
                    cur = prev.copy()
                    cur.append(num)
                    res.append(cur.copy())
                    return
                elif target - num > 0:
                    cur = prev.copy()
                    cur.append(num)
                    dfs(cur, target - num, left + i)
                else:
                    return
        dfs([], target)
        
        return res
