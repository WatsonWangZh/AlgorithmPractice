# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to find the number of connected components in an undirected graph.

# Example 1:
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#      0          3
#      |          |
#      1 --- 2    4 
# Output: 2

# Example 2:
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#      0           4
#      |           |
#      1 --- 2 --- 3
# Output:  1

# Note:
# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/319459/Python3-UnionFindDFSBFS-solution
        # M1. Simple UnionFind
        # parent = list(range(n))
        
        # def find(x):
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])
        #     return parent[x]
        
        # def union(x, y):
        #     rx, ry = find(x), find(y)
        #     if rx != ry:
        #         parent[rx] = ry 
        
        # for x, y in edges:
        #     union(x, y)
        # return len({find(i) for i in range(n)})

        # M2. UnionFind with Path Compression
        # parent = list(range(n))
        
        # def find(parent, x):
        #     # Path Compression
        #     while parent[x] != x:
        #         parent[x] = parent[parent[x]]
        #         x = parent[x]
        #     return x
        
        # def union(x, y):
        #     rx, ry = find(parent, x), find(parent, y)
        #     if rx != ry:
        #         parent[rx] = ry 
        
        # for x, y in edges:
        #     union(x, y)
        # return len({find(parent, i) for i in range(n)})

        # M3. UnionFind with Union by Rank

        parent = list(range(n))
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[rx] = ry
                rank[ry] += 1
        
        for x, y in edges:
            union(x, y)
        return len({find(i) for i in range(n)})