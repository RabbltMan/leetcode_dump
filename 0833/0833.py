from typing import List
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        popidx = []
        ist = sorted(tuple(zip(indices, sources, targets)))
        for i in range(len(ist)):
            if s[ist[i][0]: ist[i][0] + len(ist[i][1])] != ist[i][1]:
                popidx.append(i)
        for idx in popidx[ : : -1]:
            ist.pop(idx)
        adj: int = 0
        for i in ist:
            s = s[0: i[0] + adj] + i[2] + s[i[0] + len(i[1]) + adj: ]
            adj += len(i[2]) - len(i[1])
        return s