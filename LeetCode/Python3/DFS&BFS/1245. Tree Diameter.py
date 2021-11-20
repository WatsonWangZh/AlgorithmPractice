# Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  
# Each node has labels in the set {0, 1, ..., edges.length}.

# Example 1:
# Input: edges = [[0,1],[0,2]]
# Output: 2
# Explanation: 
# A longest path of the tree is the path 1 - 0 - 2.

# Example 2:
# Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# Output: 4
# Explanation: 
# A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 
# Constraints:
# 0 <= edges.length < 10^4
# edges[i][0] != edges[i][1]
# 0 <= edges[i][j] <= edges.length
# The given edges form an undirected tree.

# Hints:
# Start at any node A and traverse the tree to find the furthest node from it, let's call it B.
# Having found the furthest node B, traverse the tree from B to find the furthest node from it, lets call it C.
# The distance between B and C is the tree diameter.

class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # DFS O(n)
        # choose an arbitary node(X) and find the farthest node from it (Y). 
        # Do dfs on the node (Y) to find the farthest node from that (Z). 
        # Lomgest distance is the distance from (Y) to (Z).

        import collections
        graphG = collections.defaultdict(list)
        for u,v in edges:
            graphG[u].append(v)
            graphG[v].append(u)

        def dfs(pos):
            maxLevel = float('-inf')
            visited = set()
            stack = [(pos,0)]
            while stack:
                node, level = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                if maxLevel < level:
                    maxLevel = level
                    nodeFarthest = node
                for nei in graphG[node]:
                    stack.append((nei, level + 1))
            return (nodeFarthest, maxLevel)

        nodeFarthest, maxLevel = dfs(0)

        return dfs(nodeFarthest)[1]