# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), 
# return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column 
# from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note: You can only put the bomb at an empty cell.

# Example:
# Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# Output: 3 
# Explanation: For the given grid,
# 0 E 0 0 
# E 0 W E 
# 0 E 0 0
# Placing a bomb at (1,1) kills 3 enemies.

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # M1. Brute Force O(n^2)

        # if not grid or not grid[0]:
        #     return 0
        
        # def count_kill(loc, direction):
        #     i, j = loc
        #     di, dj = direction
        #     kills = 0
        #     while 0 <= i + di < len(grid) and 0 <= j + dj <len(grid[0]) and grid[i+di][j+dj] != "W":
        #         i = i + di
        #         j = j + dj
        #         if grid[i][j] == "E":
        #             kills += 1
        #     return kills

        # res = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '0':
        #             temp =0
        #             for direction in (-1,0), (1,0), (0, -1), (0, 1):
        #                 temp += count_kill((i,j), direction)
        #             res = max(res, temp)
        # return res

        # M2. DP O(mn)
        # https://leetcode.com/problems/bomb-enemy/discuss/367665/C%2B%2B-DP-beats-92.7-time-and-100-space-scanning-from-upper-left-then-from-lower-right
        if not grid or not grid[0]:
            return 0

        nx = len(grid)
        ny = len(grid[0])
        res = 0
        
        hits = [[0 for y in range(ny)] for x in range(nx)]
        col_cnt = [0] * ny

        for x in range(nx):
            row_cnt = 0
            for y in range(ny):
                if grid[x][y] == 'E':
                    row_cnt += 1
                    col_cnt[y] += 1
                elif grid[x][y] == 'W':
                    row_cnt = 0
                    col_cnt[y] = 0
                else:
                    # right and down res
                    hits[x][y] += row_cnt + col_cnt[y]

        col_cnt = [0] * ny

        for x in range(nx - 1, -1, -1):
            row_cnt = 0
            for y in range(ny - 1, -1, -1):
                if grid[x][y] == 'E':
                    row_cnt += 1
                    col_cnt[y] += 1
                elif grid[x][y] == 'W':
                    row_cnt = 0
                    col_cnt[y] = 0
                else:
                    # left and up res
                    hits[x][y] += row_cnt + col_cnt[y]

                    res = max(res, hits[x][y])

        return res