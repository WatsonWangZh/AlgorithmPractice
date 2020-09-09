# Two images A and B are given, represented as binary, square matrices of the same size.  
# (A binary matrix has only 0s and 1s as values.)
# We translate one image however we choose (sliding it left, right, up, or down any number of units), 
# and place it on top of the other image.  
# After, the overlap of this translation is the number of positions that have a 1 in both images.
# (Note also that a translation does not include any kind of rotation.)
# What is the largest possible overlap?

# Example 1:
# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.

# Notes: 
# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        n = len(A)
        res = 0
        for row in range(n):
            for col in range(n):
                ba = 0
                ab = 0
                for i in range(row, n):
                    for j in range(col, n):
                        if A[i][j] and B[i-row][j-col]:
                            ba += 1
                        if A[i-row][j-col] and B[i][j]:
                            ab += 1
                res = max(res, ba, ab)
        return res