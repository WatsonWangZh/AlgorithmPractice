# On an infinite plane, a robot initially stands at (0, 0) and faces north.  
# The robot can receive one of three instructions:
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

# Example 1:
# Input: "GGLLGG"
# Output: true
# Explanation: 
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

# Example 2:
# Input: "GG"
# Output: false
# Explanation: 
# The robot moves north indefinitely.

# Example 3:
# Input: "GL"
# Output: true
# Explanation: 
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

# Hints:
# Calculate the final vector of how the robot travels after executing all instructions once - 
# it consists of a change in position plus a change in direction.
# The robot stays in the circle iff (looking at the final vector) 
# it changes direction (ie. doesn't stay pointing north), or it moves 0.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 分析模拟
        # https://blog.csdn.net/fuxuemingzhu/article/details/92128721
        # M1
        # dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        # x, y = 0, 0
        # d = 0
        # for i in instructions:
        #     if i == "G":
        #         x += dirs[d][0]
        #         y += dirs[d % 4][1]
        #     elif i == "L":
        #         d = (d + 1) % 4
        #     elif i == "R":
        #         d = (d - 1) % 4
        # return (x == 0 and y == 0) or d != 0

        # M2
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y = 0, 0
        d = 0
        for i in instructions * 4:
            if i == "G":
                x += dirs[d][0]
                y += dirs[d % 4][1]
            elif i == "L":
                d = (d + 1) % 4
            elif i == "R":
                d = (d - 1) % 4
        return x == 0 and y == 0
