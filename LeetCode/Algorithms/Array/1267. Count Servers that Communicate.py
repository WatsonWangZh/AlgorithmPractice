# You are given a map of a server center, represented as a m * n integer matrix grid, 
# where 1 means that on that cell there is a server and 0 means that it is no server. 
# Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.

# Example 2:
# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other server.

# Example 3:
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other. 
# The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1

# Hints:
# Store number of computer in each row and column.
# Count all servers that are not isolated.

class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 枚举 置位 统计 O(mn)
        # 对于每一行，统计这一行中 1 位置的个数。如果个数大于 1，则修改 1 的位置为 2。
        # 对于每一列，统计这一列中 1 或 2 位置的个数。如果个数大于 1，则修改 1 的位置为 2。
        # 最后统计位置为 2 的个数。
        # 时间复杂度
        #   每个位置被遍历常数次，故时间复杂度为 O(mn)。
        # 空间复杂度
        #   仅需要常数的空间

        res = 0
        for i in range(len(grid)):
            cnt = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt += 1
            if cnt > 1:
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        grid[i][j] = 2
        
        for j in range(len(grid[0])):
            cnt = 0
            for i in range(len(grid)):
                if grid[i][j] >= 1:
                    cnt += 1
            if cnt > 1:
                for i in range(len(grid)):
                    if grid[i][j] == 1:
                        grid[i][j] = 2 
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    res += 1
        
        return res 