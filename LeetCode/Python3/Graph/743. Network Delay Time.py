# There are N network nodes, labelled 1 to N.
# Given times, a list of travel times as directed edges times[i] = (u, v, w), 
# where u is the source node, v is the target node, 
# and w is the time it takes for a signal to travel from source to target.
# Now, we send a signal from a certain node K. 
# How long will it take for all nodes to receive the signal? If it is impossible, return -1.

# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2
 
# Note:
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

# Hints:
# We visit each node at some time, and if that time is better than the fastest time we've reached this node, 
# we travel along outgoing edges in sorted order. Alternatively, we could use Dijkstra's algorithm.

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # M1. Dijkstra算法
        # 除起点外，初始化为正无穷
        D = [float('inf')] * (N+1)
        graph = {}
        for u, v, w in times:
            graph[u] = graph.get(u, []) + [(v, w)]
        visited = [0] * (N+1)
        D[K] = 0
        # 逐步确定除K外的N-1个节点
        for i in range(N-1):
            minDistance = float('inf')
            minIndex = 1
            # 找到未确定最短路径节点集合中的最小值
            for j in range(1, N+1):
                if not visited[j] and D[j] < minDistance:
                    minDistance = D[j]
                    minIndex = j
            visited[minIndex] = 1

            # 松弛操作
            if minIndex in graph.keys():
                for v, w in graph[minIndex]:
                    if not visited[v]:
                        D[v] = min(D[minIndex] + w, D[v])
        
        maxDistance = -1
        for i in range(1, N + 1):
            if D[i] == float('inf'):
                return -1
            maxDistance = max(maxDistance, D[i])
        return maxDistance

        # M2. Bellman-Ford 算法
        # 除起点外，初始化为正无穷
        D = [float('inf')] * (N+1)
        D[K] = 0
        # 进行N-1轮的松弛，因为任意两点间的最短路径最多包含 N-1 条边
        for i in range(N-1):
            # flag为该轮D改变的数量，不设flag会超时
            flag = 0
            for u, v, w in times:
                if D[u] != float('inf'):
                    if D[v] > D[u] + w:
                        D[v] = D[u] + w
                        flag += 1
            if flag == 0:
                break
            
        maxDistance = -1
        for i in range(1, N + 1):
            if D[i] == float('inf'):
                return -1
            maxDistance = max(maxDistance, D[i])

        return maxDistance