# Given a 2d grid map of '1's (land) and '0's (water), c
# ount the number of islands. An island is surrounded by water 
# and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input:
# 11110
# 11010
# 11000
# 00000
# Output: 1

# Example 2:
# Input:
# 11000
# 11000
# 00100
# 00011
# Output: 3

class Solution:
    def convertIsland(self, row, col, grid):
        grid[row][col] = '0'
        if(col < len(grid[0])-1 and grid[row][col+1] == '1'):
            self.convertIsland(row, col+1, grid)
        if(row < len(grid)-1 and grid[row+1][col] == '1'):
            self.convertIsland(row+1, col, grid)
        if(row > 0 and grid[row-1][col] == '1'):
            self.convertIsland(row-1, col, grid)
        if(col > 0 and grid[row][col-1] == '1'):
            self.convertIsland(row, col-1, grid)
        return 
    
    def numIslands(self, grid: List[List[str]]) -> int:
        # When you hit a '1', go through all the island and convert values to 0.
        # At end, this is 1 island, and then continue to find other '1's that haven't been zeroed out because they weren't in the island.
        
        if(grid == []):
            return 0
        row, col = 0, 0 
        maxRow, maxCol = len(grid),len(grid[0]) 
        count = 0
        
        for row in range(maxRow):
            for col in range(maxCol):
                if(grid[row][col] == '1'):
                    count += 1
                    self.convertIsland(row, col, grid)  
        return count
        