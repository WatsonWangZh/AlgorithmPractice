# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, 
# for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, 
# is it possible for you to finish all courses?

# Example 1:
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
# Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

class Solution:
    def canFinish(self, numCourses, prerequisites):

        # 本质就是在有向图中检测环
        # BFS 的解法，我们定义二维数组 adjLists 来表示这个有向图，一维数组 visinDegree 来表示每个顶点的入度。
        # 我们开始先根据输入来建立这个有向图，并将入度数组也初始化好。
        # 然后我们定义一个 freeNodes 变量，将所有入度为0的点放入队列中，
        # 然后开始遍历freeNodes队列，从 adjLists 里遍历其连接的点，每到达一个新节点，将其入度减一，
        # 如果此时该点入度为0，则放入队列末尾。直到遍历完队列中所有的节点，
        # 若此时还有节点的入度不为0，则说明环存在，返回 False，反之则返回 True。
        
        adjLists = [[] for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]

        for edge in prerequisites:
            inDegree[edge[0]] += 1
            adjLists[edge[1]].append(edge[0])

        freeNodes = []
        for idx, num in enumerate(inDegree):
            if num == 0:
                freeNodes.append(idx)
                
        count = 0
        while len(freeNodes):
            cur = freeNodes.pop()
            count += 1
            for v in adjLists[cur]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    freeNodes.append(v)
        
        if count == numCourses:
            return True
        else:
            return False
