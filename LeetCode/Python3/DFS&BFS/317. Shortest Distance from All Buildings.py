# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. 
# You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.

# Example:
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# Output: 7 

# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
#              the point (1,2) is an ideal empty land to build a house, as the total 
#              travel distance of 3+3+1=7 is minimal. So return 7.

# Note:
# There will be at least one building. 
# If it is not possible to build such house according to the above rules, return -1.

import collections
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # https://www.bilibili.com/video/av48806311/
        # BFS 
        
        if not grid or not grid[0]:
            return 0

        M, N = len(grid), len(grid[0])
        buildings = sum(val for line in grid for val in line if val == 1)
        canReach = [[0] * N for _ in range(M)]
        distSum = [[0] * N for _ in range(M)]
        
        def BFS(start_x, start_y):
            visited = [[False]*N for _ in range(M)]
            visited[start_x][start_y] = True
            cnt = 1
            queue = collections.deque([(start_x, start_y, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                        visited[i][j] = True
                        if grid[i][j] == 0:
                            queue.append((i,j,dist+1))
                            canReach[i][j] += 1
                            distSum[i][j] += dist+1
                        elif grid[i][j] == 1:
                            cnt += 1
                        else:
                            pass
            return cnt == buildings
        
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if not BFS(x,y): 
                        return -1
        
        ans = float('inf')
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 0 and canReach[x][y] == buildings:
                    ans = min(ans, distSum[x][y])  
        
        if ans == float('inf'):
            return -1
        return ans