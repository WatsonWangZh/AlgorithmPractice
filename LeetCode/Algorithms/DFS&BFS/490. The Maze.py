# There is a ball in a maze with empty spaces and walls. 
# The ball can go through empty spaces by rolling up, down, left or right, 
# but it won't stop rolling until hitting a wall. 
# When the ball stops, it could choose the next direction.
# Given the ball's start position, the destination and the maze, 
# determine whether the ball could stop at the destination.
# The maze is represented by a binary 2D array. 
# 1 means the wall and 0 means the empty space. 
# You may assume that the borders of the maze are all walls. 
# The start and destination coordinates are represented by row and column indexes.

# Example 1:
# Input 1: a maze represented by a 2D array
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

# Example 2:
# Input 1: a maze represented by a 2D array
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
# Output: false
# Explanation: There is no way for the ball to stop at the destination.

# Note:
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, 
# and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), 
# but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, 
# and both the width and height of the maze won't exceed 100.

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # DFS 模拟

        if not maze or not maze[0]:
            return False
        
        rows, cols = len(maze), len(maze[0])
        visited = [[0] * cols for _ in range(rows)]
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        x, y = start[0], start[1]

        def dfs(maze, visited, dirs, x, y, destination):

            visited[x][y] = 1
            
            if x == destination[0] and y == destination[1]:
                return True
            
            for dx, dy in dirs:
                # move along the direction until reach the wall
                xn, yn = x+dx, y+dy
                while 0 <= xn < rows and 0 <= yn < cols and maze[xn][yn] == 0:
                    xn += dx
                    yn += dy
                
                # move back to the last feasbile location
                xn -= dx
                yn -= dy
                
                if visited[xn][yn]:
                    continue
                    
                if dfs(maze, visited, dirs, xn, yn, destination):
                    return True
                
            return False

        return dfs(maze, visited, dirs, x, y, destination) 
        