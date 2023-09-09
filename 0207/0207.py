from collections import *
from typing import *

# 深度优先，通过visited来判断Node是否处于递归的过程中，即递归是否形成了一个环
class Solution:
    def dfs(self, num: int) -> None:
        self.visited[num] = 1
        for edgeTerminal in self.edges[num]:
            if self.visited[edgeTerminal] == 0:
                self.dfs(edgeTerminal)
                if not self.res:
                    return
            elif self.visited[edgeTerminal] == 1:
                self.res = False
                return

        self.visited[num] == 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.res = True
        self.visited = [0]*numCourses
        self.edges = defaultdict(list)

        for edge in prerequisites:
            self.edges[edge[1]].append(edge[0])

        for course in range(numCourses):
            if self.res and not self.visited[course]:
                self.dfs(course)

        return self.res