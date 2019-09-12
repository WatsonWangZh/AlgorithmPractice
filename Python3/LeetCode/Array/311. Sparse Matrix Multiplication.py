# Given two sparse matrices A and B, return the result of AB.
# You may assume that A's column number is equal to B's row number.

# Example:
# Input:
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
# Output:
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        mA,nA,nB = len(A),len(A[0]),len(B[0])
        res = [[0]*len(B[0]) for _ in range(mA)]

        for i in range(mA):
            for j in range(nA):
                if A[i][j]:
                    for k in range(nB):
                        res[i][k] += A[i][j]*B[j][k]
                        
        return res