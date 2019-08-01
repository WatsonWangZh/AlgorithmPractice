# On a N * N grid, we place some 1 * 1 * 1 cubes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
# Return the total surface area of the resulting shapes.

# Example 1:
# Input: [[2]]
# Output: 10

# Example 2:
# Input: [[1,2],[3,4]]
# Output: 34

# Example 3:
# Input: [[1,0],[0,2]]
# Output: 16

# Example 4:
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32

# Example 5:
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46

class Solution:
    def surfaceArea(self, grid):
        n = len(grid)
        res = 0
        for i in range(grid):
            for j in range(grid):
                if grid[i][j] > 0:
                    res += 4 * grid[i][j] + 2
                if i > 0:
                    res -= min(grid[i][j], grid[i - 1][j]) * 2
                if j > 0:
                    res -= min(grid[i][j], grid[i][j - 1]) * 2
        return res
