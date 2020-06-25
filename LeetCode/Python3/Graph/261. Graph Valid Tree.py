# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.

# Example 1:
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true

# Example 2:
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false

# Note: you can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # 并查集 O(n)
        if len(edges) != n-1: 
            return False
        
        parents = {}
        for i in range(n):
            parents[i] = i
        
        def find(i):
            parent = parents[i]
            if parent == i:
                return i
            parents[i] = parents[parent] # path compression
            return find(parent)
        
        for a,b in edges:
            pa, pb = find(a), find(b)
            # before union, they have the same parents already
            if pa == pb:
                return False 
            parents[pa] = pb

        return True