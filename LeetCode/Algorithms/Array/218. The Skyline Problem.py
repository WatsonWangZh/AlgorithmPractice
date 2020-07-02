# A city's skyline is the outer contour of the silhouette 
# formed by all the buildings in that city when viewed from a distance. 
# Now suppose you are given the locations and height of all the buildings 
# as shown on a cityscape photo (Figure A), write a program to output the skyline 
# formed by these buildings collectively (Figure B).

# Buildings  Skyline Contour
# The geometric information of each building is represented 
# by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x 
# coordinates of the left and right edge of the ith building, respectively, 
# and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, 
# and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on 
# an absolutely flat surface at height 0.

# For instance, the dimensions of all buildings in Figure A are recorded as: 
# [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

# The output is a list of "key points" (red dots in Figure B) in the format of 
# [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. 
# A key point is the left endpoint of a horizontal line segment. 
# Note that the last key point, where the rightmost building ends, 
# is merely used to mark the termination of the skyline, 
# and always has zero height. Also, the ground in between any 
# two adjacent buildings should be considered part of the skyline contour.

# For instance, the skyline in Figure B should be represented as:
# [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

# Notes:
# The number of buildings in any input list is guaranteed to be in the range [0, 10000].
# The input list is already sorted in ascending order by the left x position Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height in the output skyline. 
# For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; 
# the three lines of height 5 should be merged into one in the final output as such: 
# [...[2 3], [4 5], [12 7], ...]

from heapq import *
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        # https://www.youtube.com/watch?v=GSBLe8cKu0s
        # 如果按照矩形来处理将会非常麻烦，可以把这些矩形拆成两个点，一个左上顶点，一个右上顶点，
        # 这个题相当于处理2*n个边的问题，每一个边有一个x-axis和一个height，把所给的triplet转换成[x-axis, height]，
        # 对这些顶点按x-axis排序。然后开始遍历这些点，用一个最大堆来记录高度，对于左顶点，将height加入堆中。
        # 对于右顶点，从堆中移出height，同时也意味这这个矩形的结束。
        # 堆顶是所有顶点中最高的点，是当前图形的最高位置。只要这个点没被移出堆，说明这个最高的矩形还没结束。
        # 如果堆顶高度值出现了变化，说明出现了拐点，记录相应位置到结果中。
        # 具体代码中，为了在排序后的顶点列表中区分左右顶点，同一个图形的左右顶点height一个是正数值，一个是负数值
        
        for i in range(len(buildings)-1, 0, -1):
            # enclosed
            if buildings[i-1][1] >= buildings[i][1] and buildings[i-1][2] >= buildings[i][2]:
                buildings.pop(i)
            # same height connected
            elif buildings[i-1][1] >= buildings[i][0] and buildings[i-1][2] == buildings[i][2]:
                buildings[i-1][1] = buildings[i][1]
                buildings.pop(i)

        points = []
        for l,r,h in buildings:
            points += (l,-h),(r,h)
        points.sort()
        
        pq = [0]
        result = []
        
        for x, h in points:
            if h < 0: 
                # left/start point, push into queue
                if -h > -pq[0]: 
                    # new height higher
                    # , is important
                    result += [x,-h],
                heappush(pq,h)
            else: 
                # right/end point, remove and see if change height, if yes add to result
                if h == -pq[0]:
                    heappop(pq)
                    # , is important
                    result += [x,-pq[0]],
                else:
                    pq.remove(-h)
                    heapify(pq)
        return result
    