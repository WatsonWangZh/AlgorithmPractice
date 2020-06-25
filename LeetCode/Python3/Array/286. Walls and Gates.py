# You are given a m x n 2D grid initialized with these three possible values.
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF 
# as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. 
# If it is impossible to reach a gate, it should be filled with INF.

# Example: 
# Given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF

# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # M1. BFS
        # 借助queue，我们首先把门的位置都排入queue中，
        # 然后开始循环，对于门位置的四个相邻点，我们判断其是否在矩阵范围内，并且位置值是否大于上一位置的值加1，
        # 如果满足这些条件，我们将当前位置赋为上一位置加1，并将次位置排入queue中，这样等queue中的元素遍历完了，所有位置的值就被正确地更新了。

        # # base case:
        # if not rooms:
        #     return

        # row, col = len(rooms), len(rooms[0])
        # # find the index of a gate
        # q = [(i, j) for i in range(row) for j in range(col) if rooms[i][j] == 0]

        # for x, y in q:
        #     # get the distance from a gate
        #     distance = rooms[x][y]+1
        #     directions = [(-1,0), (1,0), (0,-1), (0,1)]
        #     for dx, dy in directions:
        #         new_x, new_y = x+dx, y+dy
        #         if 0 <= new_x < row and 0 <= new_y < col and rooms[new_x][new_y] > distance:
        #             # update the value
        #             rooms[new_x][new_y] = distance
        #             q.append((new_x, new_y))

        # DFS
        # 搜索0的位置，每找到一个0，以其周围四个相邻点为起点，开始DFS遍历，并带入深度值1，
        # 如果遇到的值大于当前深度值，我们将位置值赋为当前深度值，并对当前点的四个相邻点开始DFS遍历，注意此时深度值需要加1，
        # 这样遍历完成后，所有的位置就被正确地更新了。

        # base case
        if not rooms: return
        
        row, col = len(rooms), len(rooms[0])
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)
                    
    def dfs(self, rooms, x, y, dist):
        row, col = len(rooms), len(rooms[0])
        if x < 0 or x >= row or y < 0 or y >= col or rooms[x][y] < dist:
            return
        rooms[x][y] = dist
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            self.dfs(rooms, x+dx, y+dy, dist+1)
