# Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, 
# compute the volume of water it is able to trap after raining.

# Note:
# Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

# Example:
# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
# Return 4.

# The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

# After the rain, water is trapped between the blocks. The total volume of water trapped is 4.
import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        heap = []

        visited = [[0 for ii in range(n)] for jj in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1

        waterfill = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if heightMap[x][y] < height:
                        waterfill += height - heightMap[x][y]
                    visited[x][y] = 1
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
        return waterfill
