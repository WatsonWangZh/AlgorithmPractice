# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
# User Accepted:120
# User Tried:257
# Total Accepted:121
# Total Submissions:505
# Difficulty:Hard
# Given a weighted undirected connected graph with n vertices numbered from 0 to n-1,
# and an array edges where edges[i] = [fromi, toi, weighti]
# represents a bidirectional and weighted edge between nodes fromi and toi.
# A minimum spanning tree (MST) is a subset of the edges of the graph
# that connects all vertices without cycles and with the minimum possible total edge weight.
# Find all the critical and pseudo-critical edges in the minimum spanning tree (MST) of the given graph.
# An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge.
# A pseudo-critical edge, on the other hand, is that which can appear in some MSTs but not all.
# Note that you can return the indices of the edges in any order.

# Example 1:
# Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# Output: [[0,1],[2,3,4,5]]
# Explanation: The figure above describes the graph.
# The following figure shows all the possible MSTs:
# Notice that the two edges 0 and 1 appear in all MSTs,
# therefore they are critical edges, so we return them in the first list of the output.
# The edges 2, 3, 4, and 5 are only part of some MSTs,
# therefore they are considered pseudo-critical edges. We add them to the second list of the output.

# Example 2:
# Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# Output: [[],[0,1,2,3]]
# Explanation: We can observe that since all 4 edges have equal weight,
# choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
 
# Constraints:
# 2 <= n <= 100
# 1 <= edges.length <= min(200, n * (n - 1) / 2)
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti <= 1000
# All pairs (fromi, toi) are distinct.

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def kruskal(removed, parent, mst_w, k):
            def find(x):
                if x != parent[x]:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                px, py = find(x), find(y)
                if px == py:
                    return False
                parent[px] = py
                return True

            for _from, _to, w in sorted(edges, key=lambda x: x[2]):
                edge = [_from, _to, w]
                if edge == removed:
                    continue
                if union(_from, _to):
                    mst_w += w
                    k += 1
            return mst_w if k == n else float('inf')

        res = [[], []]
        # Original MST weight by considering all edges
        mst_w = kruskal(None, [i for i in range(n)], 0, 1)

        for i, edge in enumerate(edges):

            # remove this edge and see if MST weight has increased, if yes -> critical edge
            rem_w = kruskal(edge, [i for i in range(n)], 0, 1)
            if rem_w > mst_w:
                res[0].append(i)
            else:
                # If hasn't increased, add this edge to the DSU initial values and see if MST weight remains same,
                # if yes -> pseudo critical edge
                parent = [i for i in range(n)]
                parent[edge[0]] = edge[1]
                add_w = kruskal(edge, parent, edge[2], 2)
                if add_w == mst_w:
                    res[1].append(i)
        return res