# Given a list of non-overlapping axis-aligned rectangles rects, 
# write a function pick which randomly and uniformily 
# picks an integer point in the space covered by the rectangles.

# Note:
# An integer point is a point that has integer coordinates. 
# A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
# ith rectangle = rects[i] = [x1,y1,x2,y2], 
# where [x1, y1] are the integer coordinates of the bottom-left corner, 
# and [x2, y2] are the integer coordinates of the top-right corner.
# length and width of each rectangle does not exceed 2000.
# 1 <= rects.length <= 100
# pick return a point as an array of integer coordinates [p_x, p_y]
# pick is called at most 10000 times.

# Example 1:
# Input: 
# ["Solution","pick","pick","pick"]
# [[[[1,1,5,5]]],[],[],[]]
# Output: 
# [null,[4,1],[4,1],[3,3]]

# Example 2:
# Input: 
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# Output: 
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
# Explanation of Input Syntax:
# The input is two lists: the subroutines called and their arguments. 
# Solution's constructor has one argument, the array of rectangles rects. 
# pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

from bisect import bisect_left
from random import randint
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weight = [] #按序累加每个矩形的面积（即权重）
        s = 0
        for rect in rects:
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) #注意加1
            s += area
            self.weight.append(s)


    def pick(self) -> List[int]:
        #从[1，所有矩形权重之和]，随机选择一个数。在weight数组中二分查找对应矩形（的下标）
        #显然，某个矩形被选中的概率正比于矩形面积
        index = bisect_left(self.weight, randint(1, self.weight[-1]))
        rect = self.rects[index] #选中的矩形
        return [randint(rect[0], rect[2]), randint(rect[1], rect[3])]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()