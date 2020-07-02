# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# Example 1:
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# Example 2:
# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
 
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # M1. 蛮力 O((mn)^2) O(mn) TLE
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf')] *n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    for k in range(m):
                        for l in range(n):
                            if matrix[k][l] == 0:
                                dist[i][j] = min(dist[i][j], abs(k-i)+abs(l-j))
                                
        return dist

        # M2. BFS
        m, n = len(matrix), len(matrix[0])
        q = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')
                else:
                    q.append((i, j))
        while q:
            new_q = []
            for i, j in q:
                for r, c in ((i, j+1),(i, j-1), (i+1, j), (i-1, j)):
                    z = matrix[i][j] + 1
                    if 0 <= r < m and 0 <= c < n and matrix[r][c] > z:
                        matrix[r][c] = z
                        new_q.append((r, c))
            q = new_q
        return matrix

        # M3. DP
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf')] *n for i in range(m)]
        
        # left and top directions
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j] + 1, dist[i][j-1]+1)
                else:
                    dist[i][j] = 0

        # right and bottom direction
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] != 0:
                    if i < m-1:
                        dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                    if j < n-1:
                        dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
        return dist