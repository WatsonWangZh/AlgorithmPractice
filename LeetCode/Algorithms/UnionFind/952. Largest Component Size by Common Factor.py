# Given a non-empty array of unique positive integers A, consider the following graph:
# There are A.length nodes, labelled A[0] to A[A.length - 1];
# There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.

# Example 1:
# Input: [4,6,15,35]
# Output: 4

# Example 2:
# Input: [20,50,9,63]
# Output: 2

# Example 3:
# Input: [2,3,6,7,4,12,21,39]
# Output: 8

# Note:
# 1 <= A.length <= 20000
# 1 <= A[i] <= 100000

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DisjointSetUnion(max(A))

        # attribute each element in A
        #   to all the groups that lead by its factors.
        for a in A:
            for factor in range(2, int(sqrt(a))+1):
                if a % factor == 0:
                    dsu.union(a, factor)
                    dsu.union(a, a // factor)

        # count the size of group one by one
        max_size = 0
        group_count = defaultdict(int)
        for a in A:
            group_id = dsu.find(a)
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id])

        return max_size


class DisjointSetUnion(object):

    def __init__(self, size):
        # initially, each node is an independent component
        self.parent = [i for i in range(size+1)]
        # keep the size of each component
        self.size = [1] * (size+1)
    
    def find(self, x):
        """ return the component id that the element x belongs to. """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """ merge the two components that x, y belongs to respectively,
              and return the merged component id as the result.
        """
        px, py = self.find(x), self.find(y)
        
        # the two nodes share the same set
        if px == py:
            return px
        
        # otherwise, connect the two sets (components)
        if self.size[px] > self.size[py]:
            # add the node to the union with less members.
            # keeping px as the index of the smaller component
            px, py = py, px
        # add the smaller component to the larger one
        self.parent[px] = py
        self.size[py] += self.size[px]
        # return the final (merged) group
        return py
