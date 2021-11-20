# There are N cities numbered from 1 to N.
# You are given connections, 
# where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)
# Return the minimum cost so that for every pair of cities, 
# there exists a path of connections (possibly of length 1) that connects those two cities together.  
# The cost is the sum of the connection costs used. If the task is impossible, return -1.

# Example 1:
# Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
# Output: 6
# Explanation: 
# Choosing any 2 edges will connect all cities so we choose the minimum 2.

# Example 2:
# Input: N = 4, connections = [[1,2,3],[3,4,4]]
# Output: -1
# Explanation: 
# There is no way to connect all cities even if all edges are used.
 
# Note:
# 1 <= N <= 10000
# 1 <= connections.length <= 10000
# 1 <= connections[i][0], connections[i][1] <= N
# 0 <= connections[i][2] <= 10^5
# connections[i][0] != connections[i][1]

# Hints:
# What if we model the cities as a graph?
# Build a graph of cities and find the minimum spanning tree.
# You can use a variation of the Kruskal's algorithm for that.
# Sort the edges by their cost and use a union-find data structure.
# How to check all cities are connected?
# At the beginning we have n connected components, 
# each time we connect two components the number of connected components is reduced by one. 
# At the end we should end with only a single component otherwise return -1.

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # M1. Kruskal算法
        if len(connections) < N - 1:
            return -1
        connections.sort(key=lambda a : a[2])
        parent = [i for i in range(N)]
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        res, e, k = 0, 0, 0
        while e < N - 1:
            u, v, w = connections[k]
            k += 1
            x, y = find(u-1), find(v-1)
            if x != y:
                e += 1
                res += w
                parent[x] = y        
        return res

        # M2. Prim算法
        if len(connections) < N - 1:
            return -1
        graph = {}
        for u, v, w in connections:
            graph[(u, v)] = w
        now = [1]
        res = 0
        for i in range(N-1):
            minNode = 0
            minDis = float('inf')
            for j in range(N + 1):
                for x in now:
                    if j not in now and (x, j) in graph.keys():
                        if graph[(x, j)] < minDis:
                            minDis = graph[(x, j)]
                            minNode = j
            res += minDis
            now.append(minNode)
        return res