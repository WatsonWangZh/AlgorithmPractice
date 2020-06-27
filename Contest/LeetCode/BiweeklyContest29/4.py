# 1494. Parallel Courses II
# User Accepted:662
# User Tried:1871
# Total Accepted:739
# Total Submissions:4260
# Difficulty:Hard
# Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.
# In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.
# Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.

# Example 1:
# Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
# Output: 3 
# Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.

# Example 2:
# Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
# Output: 4 
# Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.

# Example 3:
# Input: n = 11, dependencies = [], k = 2
# Output: 6
 
# Constraints:
# 1 <= n <= 15
# 1 <= k <= n
# 0 <= dependencies.length <= n * (n-1) / 2
# dependencies[i].length == 2
# 1 <= xi, yi <= n
# xi != yi
# All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
# The given graph is a directed acyclic graph.

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        
        if not dependencies:
            return math.ceil(n/k)
        
        courseTaken, semesterCount = [], 0
        
        # a. initialise the graph
        inDegree = {}
        outDegree = {}
        graph = {}
        
        for i in range(1, n + 1):
            inDegree[i] = 0
            outDegree[i] = 0
            graph[i] = []

        # b. build graph
        for dependency in dependencies:
            courseX, courseY = dependency[0], dependency[1]
            graph[courseX].append(courseY)
            inDegree[courseY] += 1
            outDegree[courseX] += 1

        # c. find all sources. all vertices with 0 inDegree
        sources = []
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the courseTaken and subtract one from all of its children's in-degrees
        # if a child's in-degree becomes zero, add it to the sources queue
        while sources:
            sources.sort(key=lambda x: -outDegree[x])
            # print(sources, courseCountForThisSemester, semesterCount)
            semesterCount += 1
            courseCountForThisSemester = min(len(sources), k)  # take a course on this semester
            for _ in range(courseCountForThisSemester):
                vertex = sources.pop(0)
                courseTaken.append(vertex)
                for child in graph[vertex]:
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        sources.append(child)

        if len(courseTaken) != n: # We were not able to take all the course because of a cyclic dependency
            return -1
        
        return semesterCount