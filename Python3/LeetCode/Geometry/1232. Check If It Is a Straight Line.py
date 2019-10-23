# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY plane.

# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
 
# Constraints:
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.

# Hints:
# If there're only 2 points, return true.
# Check if all other points lie on the line defined by the first 2 points.
# Use cross product to check collinearity.

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # The slope for a line through any 2 points (p, q) and (u, v) is (q - v) / (p - u); 
        # Therefore, for any given 3 points (denote the 3rd point as (x, y)), 
        # if they are in a straight line, the slopes of the lines from the 3rd point to the other 2 points respectively must be equal:
        # (y - q) / (x - p) = (y - v) / (x - u)
        # In order to avoid being divided by 0, use multiplication form:
        # (x - u) * (y - q) = (x - p) * (y - v)
        # Now imagine connecting the first 2 points respectively with others one by one, Check if all of the slopes are equal.

        if len(coordinates) == 2:
            return True
        # 斜率公式 转化消除除数为0的问题  
        (u, v), (p, q) = coordinates[: 2]
        for x, y in coordinates:
            if (x - u) * (y - q) != (x - p) * (y - v):
                return False
        return True

        # One Line
        # (u, v), (p, q) = coordinates[: 2]
        # return all((x - u) * (y - q) == (x - p) * (y - v) for x, y in coordinates)        