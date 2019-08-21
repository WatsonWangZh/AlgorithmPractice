# There are N students in a class. Some of them are friends, while some are not. 
# Their friendship is transitive in nature. For example, if A is a direct friend of B, 
# and B is a direct friend of C, then A is an indirect friend of C. 
# And we defined a friend circle is a group of students who are direct or indirect friends.

# Given a N*N matrix M representing the friend relationship between students in the class. 
# If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
# And you have to output the total number of friend circles among all the students.

# Example 1:
# Input: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
# The 2nd student himself is in a friend circle. So return 2.

# Example 2:
# Input: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.

class unionFindSet:
        def __init__(self, S):
                self.root = {i:i for i in S}
                self.count = len(S)  #number of different componets

        def find(self, u): #find root (the node whose parent is itself)
                while self.root[u]!=u:
                        u = self.root[u]
                return u


        def union(self, u, v):
                pu, pv = self.find(u), self.find(v)
                if pu == pv:
                        return False
                self.root[pu] = pv
                self.count -= 1 #update count
                return True

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # 并查集 O(n^2)
        # 此题为并查集的入门题。
        # 基础的并查集能解决的一类问题是不断将两个元素所在集合合并，并随时询问两个元素是否在同一集合。
        # 定义数组 f(i) 表示 i 元素所在集合的根结点（代表元素）。初始时，所有元素所在集合的根结点就是自身。
        # 合并时，直接将两个集合的根结点合并，即修改 f 数组。
        # 查询时，不断通过判断 i 是否等于 f(i) 的操作，若不相等则递归判断 f(f(i))，直到 i == f(i) 为止。
        # 但以上做法会在一条链的情况下单次查询的时间复杂度退化至线性，故可以采用路径压缩优化，将复杂度降到近似常数。
        # 读者可以自行查阅相关资料。
        # 对于此题，最后只需检查有多少个元素为一个集合的根结点即可。
        # 时间复杂度
        # 并查集单次操作的复杂度近似于常数，故总时间复杂度为遍历整个朋友关系数组的复杂度，即 O(n^2)。

        n = len(M)
        data = unionFindSet([i for i in range(n)])
        for i in range(n-1):
                for j in range(i+1, n):
                        if M[i][j]==1:
                                data.union(i, j)
        return data.count