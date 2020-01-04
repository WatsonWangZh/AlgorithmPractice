# Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
# Example:
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 模拟 O(n^2)
        res = [[0] * n for _ in range(n)]
        dx, dy, d = [-1, 0, 1, 0], [0, 1, 0, -1], 0
        x, y = 0, 0

        for i in range(n*n):
            res[x][y] = i+1
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or res[nx][ny]:
                d = (d+1) % 4
                nx, ny = x+dx[d], y+dy[d]
            x, y = nx, ny
            
        return res