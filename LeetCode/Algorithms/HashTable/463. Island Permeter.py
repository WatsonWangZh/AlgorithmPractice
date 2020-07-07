# You are given a map in form of a two-dimensional integer grid 
# where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island 
# (i.e., one or more connected land cells).
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
# One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 
# Example:
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # M1. 模拟 O(4mn)
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    zero_count = 0
                    for delta_r, delta_c in [(0,1), (0, -1), (-1, 0), (1, 0)]:
                        new_r = r + delta_r
                        new_c = c + delta_c
                        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                            if grid[new_r][new_c] == 0:
                                zero_count += 1
                        else:
                            zero_count += 1
                    res += zero_count
        return res

        # M2. 统计邻居 O(2mn)
        # 初始时，每个island有4条边，每多一个邻居island，二者相交处的边数-2
        # 由于遍历是自上而下，自左至右的，可以利用上一步中信息，只统计下面和右边的邻居陆地即可，
        # 减少重复计算，提高常数倍时间复杂度。
         
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res += 4
                    
                    if r > 0 and grid[r-1][c] == 1:
                        res -= 2
                        
                    if c > 0 and grid[r][c-1] == 1:
                        res -= 2
        
        return res
