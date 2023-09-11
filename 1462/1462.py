from typing import *

'''
(a := [[]] * 3) == (b := [[] for _ in range(3)]) == True

a[1].append(0)
b[1].append(0)

(a == b) == False
a = [[0], [0], [0]]
b = [[], [0], []]
'''

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        directPreTable = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            directPreTable[pre[0]].append(pre[1])
        res = []
        visited = [False] * numCourses
        isPre = [[False] * numCourses for _ in range(numCourses)]

        def dfs(course: int):
            if (visited[course]):
                return
            visited[course] = True
            for pre in directPreTable[course]:
                dfs(pre)
                isPre[course][pre] = True
                for i in range(numCourses):
                    isPre[course][i] = isPre[course][i] or isPre[pre][i]

        for course in range(numCourses):
            dfs(course)

        for query in queries:
            res.append(isPre[query[0]][query[1]])

        return res
