# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.

# Note: The length of each dimension in the given grid does not exceed 50.

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 递归DFS
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        res = 0
        def dfs(row, col):
            if 0<=row<rows and 0<=col<cols and grid[row][col]:
                grid[row][col] = 0
                return 1 + dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1)
            else:
                return 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    res = max(res, dfs(row, col))
        return res

        # 队列BFS
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        def bfs(grid, row, col):
            q = [(row, col)]
            grid[row][col] = 0
            res = 1
            while q:
                q2 = []
                for row, col in q:
                    if row + 1 < rows and grid[row + 1][col] == 1:
                        grid[row + 1][col] = 0
                        q2.append((row+1, col))
                        res += 1
                    if row - 1 >= 0 and grid[row-1][col] == 1:
                        grid[row-1][col] = 0
                        q2.append((row-1, col))
                        res += 1
                    if col + 1 < cols and grid[row][col+1] == 1:
                        grid[row][col+1] = 0
                        q2.append((row, col+1))
                        res += 1
                    if col - 1 >= 0 and grid[row][col-1] == 1:
                        grid[row][col-1] = 0
                        q2.append((row, col-1))
                        res += 1
                q = q2
            return res

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    res = max(res, bfs(grid, row, col))
        return res