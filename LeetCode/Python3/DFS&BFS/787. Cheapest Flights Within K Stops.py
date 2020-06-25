# There are n cities connected by m flights. 
# Each flight starts from city u and arrives at v with a price w.
# Now given all the cities and flights, 
# together with starting city src and the destination dst, 
# your task is to find the cheapest price from src to dst with up to k stops. 
# If there is no such route, output -1.

# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200

# Explanation: 
# The graph looks like this:
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500

# Explanation: 
# The graph looks like this:
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 
# Constraints:
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.

# M1. DFS 
import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        graph = collections.defaultdict(dict)
        for u, v, e in flights:
            graph[u][v] = e
            
        visited = [0] * n

        res = [float('inf')]
        # python在递归函数中的传参问题
        # https://blog.csdn.net/li123_123_/article/details/99203165

        self.dfs(graph, src, dst, K + 1, 0, visited, res)
        return -1 if res[0] == float('inf') else res[0]

    def dfs(self, graph, src, dst, k, cost, visited, res):
        
        if src == dst:
            res[0] = cost
            return
        
        if k == 0:
            return
        
        for v, e in graph[src].items():
            if visited[v]: continue
            if cost + e > res[0]: continue
            visited[v] = 1
            self.dfs(graph, v, dst, k - 1, cost + e, visited, res)
            visited[v] = 0


# M2. BFS
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        graph = collections.defaultdict(dict)
        for u, v, e in flights:
            graph[u][v] = e
            
        res = float('inf')
        que = collections.deque()
        que.append((src, 0))
        step = 0
        
        while que:
            size = len(que)
            for i in range(size):
                cur, cost = que.popleft()
                if cur == dst:
                    res = min(res, cost)
                    
                for v, w in graph[cur].items():
                    if cost + w > res:
                        continue
                    que.append((v, cost + w))
                    
            if step > K: break
            step += 1
            
        return -1 if res == float('inf') else res
