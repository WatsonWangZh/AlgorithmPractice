# On a 2-dimensional grid, there are 4 types of squares:
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, 
# that walk over every non-obstacle square exactly once.

# Example 1:
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

# Example 2:
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

# Example 3:
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation: 
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
 
# Note:
# 1 <= grid.length * grid[0].length <= 20

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        zero_cnt = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1: 
                    zero_cnt += 1
                if val == 1: 
                    sr, sc = r, c
                if val == 2: 
                    tr, tc = r, c

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        self.res = 0
        
        def dfs(r, c, zero_cnt):
            zero_cnt -= 1
            if zero_cnt < 0: 
                return
            if r == tr and c == tc:
                if zero_cnt == 0:
                    self.res += 1
                return

            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, zero_cnt)
            grid[r][c] = 0

        dfs(sr, sc, zero_cnt)
        return self.res
