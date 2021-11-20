# 1504. Count Submatrices With All Ones
# User Accepted:1673
# User Tried:2441
# Total Accepted:1753
# Total Submissions:3713
# Difficulty:Medium
# Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

# Example 1:
# Input: mat = [[1,0,1],
#               [1,1,0],
#               [1,1,0]]
# Output: 13
# Explanation:
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2. 
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

# Example 2:
# Input: mat = [[0,1,1,0],
#               [0,1,1,1],
#               [1,1,1,0]]
# Output: 24
# Explanation:
# There are 8 rectangles of side 1x1.
# There are 5 rectangles of side 1x2.
# There are 2 rectangles of side 1x3. 
# There are 4 rectangles of side 2x1.
# There are 2 rectangles of side 2x2. 
# There are 2 rectangles of side 3x1. 
# There is 1 rectangle of side 3x2. 
# Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.

# Example 3:
# Input: mat = [[1,1,1,1,1,1]]
# Output: 21

# Example 4:
# Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
# Output: 5
 
# Constraints:
# 1 <= rows <= 150
# 1 <= columns <= 150
# 0 <= mat[i][j] <= 1

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        M, N = len(mat), len(mat[0])

        count = [[0] * N for _ in range(M)]
        # print(count)
        for row in range(M):
            for col in range(N):
                if mat[row][col] == 1:
                    count[row][col] = 1 + count[row][col - 1] if col > 0 else 1
        
        res = 0
        for row in range(M):
            for col in range(N):
                j = row
                min_val = float('inf')
                while j >= 0 and count[j][col] > 0:
                    min_val = min(min_val, count[j][col])
                    res += min_val
                    j -= 1
        return res