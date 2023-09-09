from collections import *
from typing import *

class Solution:
    def dfs(self, course: int) -> None:
        self.visited[course] = 1
        for prerequisite in self.edges[course]:
            if (self.visited[prerequisite] == 0 and self.valid):
                self.dfs(prerequisite)
            elif (self.visited[prerequisite] == 1):
                self.valid = False
                return
        self.visited[course] = 2
        self.courseOrder.append(course)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited = [0] * numCourses
        self.edges = defaultdict(list)
        self.courseOrder = []
        self.valid = True

        for start, end in prerequisites:
            self.edges[end].append(start)

        for i in range(numCourses):
            if (not self.valid):
                return []
            if (self.visited[i] == 0):
                self.dfs(i)
            

        return self.courseOrder[::-1]
    