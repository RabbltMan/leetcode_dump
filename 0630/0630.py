from typing import *
from sortedcontainers import SortedList

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        courseList, time = SortedList(), 0

        for course in courses:
            if (time + course[0] <= course[1]):
                courseList.add(course)
                time += course[0]
            elif (courseList and courseList[-1][0] > course[0]):
                time -= courseList[-1][0] - course[0]
                courseList.pop()
                courseList.add(course)

        return len(courseList)
    