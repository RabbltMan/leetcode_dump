from typing import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        N = 2 * n
        ans = []
        path = [''] * N
        def dfs(i: int, open: int):
            if (i == N):
                ans.append(''.join(path))
                return
            if (open < n):
                path[i] = '('
                dfs(i+1, open+1)
            if (i - open < open):
                path[i] = ')'
                dfs(i+1, open)
        dfs(0, 0)

        return ans
