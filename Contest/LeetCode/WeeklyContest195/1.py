# 5448. Path Crossing
# User Accepted:3900
# User Tried:4510
# Total Accepted:4437
# Total Submissions:8514
# Difficulty:Easy
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise.

# Example 1:
# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.

# Example 2:
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
 
# Constraints:
# 1 <= path.length <= 10^4
# path will only consist of characters in {'N', 'S', 'E', 'W}

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = set()
        visited.add((x, y))

        for p in path:
            if p == 'N':
                x += 1
            if p == 'E':
                y += 1
            if p == 'W':
                y -= 1
            if p == 'S':
                x -= 1
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
      
        return False
