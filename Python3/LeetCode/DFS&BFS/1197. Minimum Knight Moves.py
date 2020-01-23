# In an infinite chess board with coordinates from -infinity to +infinity, 
# you have a knight at square [0, 0].
# A knight has 8 possible moves it can make, as illustrated below. 
# Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
# Return the minimum number of steps needed to move the knight to the square [x, y].  
# It is guaranteed the answer exists.

# Example 1:
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]

# Example 2:
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 
# Constraints:
# |x| + |y| <= 300

# Hints:
# You can simulate the movements since the limits are low.
# Is there a search algorithm applicable to this problem?
# Since we want the minimum number of moves, we can use Breadth First Search.

class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # M1. 普通BFS Time Limit Exceeded
        dst = (x, y)
        start = (0, 0)
        dirs = [
            (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)
        ]
        cell_to_moves = {start: 0}
        from collections import deque
        queue = deque([start])

        # 范围限制
        Max_X, Max_Y = abs(x) + 6, abs(y) + 6

        while queue:
            cell = queue.popleft()
            moves = cell_to_moves[cell]
            if cell == dst:
                return moves
            x, y = cell

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if abs(nx) > Max_X or abs(ny) > Max_Y:
                    continue
                next_cell = (nx, ny)
                old_moves = cell_to_moves.get(next_cell, None)
                if old_moves == None:
                    queue.append(next_cell)
                    cell_to_moves[next_cell] = moves + 1


        # M2. 优化BFS 根据对称性，将目标点限制为第一象限
        x, y = abs(x), abs(y)
        dst = (x, y)
        start = (0, 0)
        dirs = [
            (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)
        ]
        cell_to_moves = {start: 0}
        from collections import deque
        queue = deque([start])

        # 范围限制
        Max_X, Max_Y = x + 6, y + 6

        while queue:
            cell = queue.popleft()
            moves = cell_to_moves[cell]
            if cell == dst:
                return moves

            x, y = cell
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if not (-6 < nx < Max_X and -6 < ny < Max_Y):
                    continue
                next_cell = (nx, ny)
                old_moves = cell_to_moves.get(next_cell, None)
                if old_moves is None:
                    queue.append(next_cell)
                    cell_to_moves[next_cell] = moves + 1
