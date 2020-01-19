# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # M1. 模拟
        res = []
        for i in range(numRows):
            tmp = [None for _ in range(i+1)]
            tmp[0], tmp[-1] = 1, 1
            for j in range(1, i):
                tmp[j] = res[i-1][j-1] + res[i-1][j]
            res.append(tmp)
        return res

        # M2. 另一种模拟写法
        res = [[1] * n for n in range(1, numRows+1)]
        for i in range(1, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j] 
        return res