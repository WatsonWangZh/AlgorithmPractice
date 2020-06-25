# There is a brick wall in front of you. 
# The wall is rectangular and has several rows of bricks. 
# The bricks have the same height but different width. 
# You want to draw a vertical line from the top to the bottom 
# and cross the least bricks.
# The brick wall is represented by a list of rows. 
# Each row is a list of integers representing 
# the width of each brick in this row from left to right.
# If your line go through the edge of a brick, 
# then the brick is not considered as crossed. 
# You need to find out how to draw the line to cross 
# the least bricks and return the number of crossed bricks.
# You cannot draw a line just along one of the two vertical edges of the wall, 
# in which case the line will obviously cross no bricks.

# Example:
# Input: [[1,2,2,1],
#         [3,1,2],
#         [1,3,2],
#         [2,4],
#         [3,1,2],
#         [1,3,1,1]]
# Output: 2

# Note:
# The width sum of bricks in different rows are the same and won't exceed INT_MAX.
# The number of bricks in each row is in range [1,10,000]. 
# The height of wall is in range [1,10,000]. 
# Total number of bricks of the wall won't exceed 20,000.

import collections
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # 贪心，哈希表 O(nm)
        # 显然最优的线一定是沿某个块砖的边缘穿过的。
        # 统计每一行的砖可以从左到右可以构成的长度值，用哈希表统计长度值出现的次数。
        # 出现次数最多的值就应该是这条线所在的位置。
        # 时间复杂度
        # 每块砖遍历一次，哈希表单次操作的是时间复杂度为 O(1)，
        # 故总时间复杂度为砖的数量，即 O(nm)。
        
        brickcounts = collections.defaultdict(int)

        for brickline in wall:
            cut_loc = 0
            # Should not cut the wall at the end edge so excluding last elemnet.
            for brick in brickline[:-1]: 
                cut_loc += brick
                brickcounts[cut_loc] += 1 #Cut at this location.

        if brickcounts:
            result = len(wall) - max(brickcounts.values())
        else:
            result = len(wall)
        return result
