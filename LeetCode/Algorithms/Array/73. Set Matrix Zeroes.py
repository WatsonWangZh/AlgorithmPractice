# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:
# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]

# Example 2:
# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]

# Follow up:
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

# Hints:
# If any cell of the matrix has a zero we can record its row and column number using additional memory. 
# But if you don't want to use extra memory then you can manipulate the array instead. i.e. simulating exactly what the question says.
# Setting cell values to zero on the fly while iterating might lead to discrepancies. 
# What if you use some other integer value as your marker? There is still a better approach for this problem with 0(1) space.
# We could have used 2 sets to keep a record of rows/columns which need to be set to zero. 
# But for an O(1) space solution, you can use one of the rows and and one of the columns to keep track of this information.
# We can use the first cell of every row and column as a flag. This flag would determine whether a row or column has been set to zero.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # M1. 两遍遍历 一遍置标志位 一遍修改
        if not matrix:
            return 
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for tmp in range(m):
                        if matrix[tmp][j] != 0:
                            matrix[tmp][j] = 'm'
                    for tmp in range(n):
                        if matrix[i][tmp] != 0:
                            matrix[i][tmp] = 'm'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'm':
                    matrix[i][j] = 0

        # M2. Strange Method but much faster.
        # 非常无聊的一道题。解题点就在于清空标志位存在哪里的问题。可以创建O(m+n)的数组来存储，但此题是希望复用已有资源。这里可以选择第一行和第一列来存储标志位。
        # 1.先确定第一行和第一列是否需要清零
        # 2.扫描剩下的矩阵元素，如果遇到了0，就将对应的第一行和第一列上的元素赋值为0
        # 3.根据第一行和第一列的信息，已经可以讲剩下的矩阵元素赋值为结果所需的值了
        # 4.根据1中确定的状态，处理第一行和第一列。
        # https://fisherlei.blogspot.com/2013/01/leetcode-set-matrix-zeroes.html

        if not matrix:
            return 
        m, n = len(matrix), len(matrix[0])
        row2zero, col2zero = False, False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        row2zero = True
                    if j == 0:
                        col2zero = True
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if row2zero:
            for j in range(n):
                matrix[0][j] = 0
        if col2zero:
            for i in range(m):
                matrix[i][0] = 0