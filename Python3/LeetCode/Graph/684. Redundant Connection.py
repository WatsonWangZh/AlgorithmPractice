# In this problem, a tree is an undirected graph that is connected and has no cycles.
# The given input is a graph that started as a tree with N nodes 
# (with distinct values 1, 2, ..., N), with one additional edge added. 
# The added edge has two different vertices chosen from 1 to N, 
# and was not an edge that already existed.
# The resulting graph is given as a 2D-array of edges. 
# Each element of edges is a pair [u, v] with u < v, 
# that represents an undirected edge connecting nodes u and v.
# Return an edge that can be removed so that the resulting graph is a tree of N nodes. 
# If there are multiple answers, return the answer 
# that occurs last in the given 2D-array. 
# The answer edge [u, v] should be in the same format, with u < v.

# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3

# Example 2:
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3

# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, 
# where N is the size of the input array.

# Update (2017-09-26):
# We have overhauled the problem description + test cases 
# and specified clearly the graph is an undirected graph. 
# For the directed graph follow up please see Redundant Connection II). 
# We apologize for any inconvenience caused.

class unionFindSet:
    def __init__(self, nodes):
        self.root = {i:i for i in nodes}

    def find(self, u):
        if u not in self.root:
                return False
        while self.root[u] !=  u:
                u = self.root[u]
        return u

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
                return
        self.root[pu] = pv

    def add(self, k):
        self.root[k] = k

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 并查集 O(n)
        # 出现环的条件是某条边的两个端点原本就是连通的，那么加上了这条边以后就产生了环，
        # 因此我们在加入每条边的时候需要判断一下边的两个端点本身是不是连通的即可。
        # 时间复杂度分析：
        # 需要遍历一遍输入的边，对每条边的两个端点进行一下合并操作，合并的复杂度是常数的，
        # 所以复杂度为O(n)。
        
        UF = unionFindSet([])
        for edge in edges:
                if edge[0] not in UF.root:
                        UF.add(edge[0])
                if edge[1] not in UF.root:
                        UF.add(edge[1])
                if UF.find(edge[0]) == UF.find(edge[1]):
                        return edge
                else:
                        UF.union(edge[0], edge[1])
