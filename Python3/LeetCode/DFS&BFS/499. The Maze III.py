# There is a ball in a maze with empty spaces and walls. 
# The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), 
# but it won't stop rolling until hitting a wall. 
# When the ball stops, it could choose the next direction. T
# here is also a hole in this maze. 
# The ball will drop into the hole if it rolls on to the hole.
# Given the ball position, the hole position and the maze, 
# find out how the ball could drop into the hole by moving the shortest distance. 
# The distance is defined by the number of empty spaces traveled by the ball from the start position 
# (excluded) to the hole (included). 
# Output the moving directions by using 'u', 'd', 'l' and 'r'. 
# Since there could be several different shortest ways, 
# you should output the lexicographically smallest way. 
# If the ball cannot reach the hole, output "impossible".
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
# You may assume that the borders of the maze are all walls. 
# The ball and the hole coordinates are represented by row and column indexes.

# Example 1:
# Input 1: a maze represented by a 2D array
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (0, 1)
# Output: "lul"
# Explanation: There are two shortest ways for the ball to drop into the hole.
# The first way is left -> up -> left, represented by "lul".
# The second way is up -> left, represented by 'ul'.
# Both ways have shortest distance 6, 
# but the first way is lexicographically smaller because 'l' < 'u'.
#  So the output is "lul".

# Example 2:
# Input 1: a maze represented by a 2D array
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (3, 0)
# Output: "impossible"
# Explanation: The ball cannot reach the hole.

# Note:
# There is only one ball and one hole in the maze.
# Both the ball and hole exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), 
# but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.

from collections import heapq
class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int] 
        :rtype: str
        """
        # DFS
        self.m = len(maze)
        self.n = len(maze[0])
        distance = [[float('inf')] * self.n for _ in range(self.m)]
        distance[ball[0]][ball[1]] = 0
        ans = [float("inf"), ""]
        direct = {(-1,0):"u", (1,0):"d", (0,-1):"l", (0,1):"r"}

        def dfs(curr, path, ans):
            [i,j] = curr
            for (dx, dy) in ((-1,0),(1,0),(0,-1),(0,1)):
                x, y = i, j
                count = 0
                while 0 <= x < len(maze) and 0 <= y< len(maze[0]) and maze[x][y] != 1:
                    x, y = x + dx , y + dy
                    count += 1
                    if [x,y] == hole: 
                        if distance[i][j] + count < ans[0] or distance[i][j] + count == ans[0] and path + direct[(dx,dy)] < ans[1]: 
                            ans[0] = distance[i][j] + count
                            ans[1] = path + direct[(dx, dy)]       
                        return                    
                if distance[i][j] + count - 1 < ans[0] and distance[x-dx][y-dy] >= distance[i][j] + count - 1 and count != 1:
                    distance[x-dx][y-dy] = distance[i][j] + count - 1
                    dfs([x-dx, y-dy], path + direct[(dx, dy)], ans)

        dfs(ball, "",  ans)
        return ans[1] if ans[1] else "impossible"