# Given a 2D binary matrix filled with 0's and 1's, 
# find the largest rectangle containing only 1's and return its area.

# Example:
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 单调栈 O(nm)
        # 将 84. Largest Rectangle in Histogram问题扩展到二维。
            # 一行一行考虑，类比上一题，一行内所有柱形条的高度heights就是当前(i,j)位置能往上延伸的最大高度。
            # 直接套用Largest Rectangle in Histogram的单调栈算法即可。
        # 时间复杂度
            # 枚举每一行的时间复杂度是O(n)，行内单调栈的时间复杂度是O(m)，故总时间复杂度为O(nm)。
        # https://www.cnblogs.com/grandyang/p/4322667.html

        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        result = 0
        for row in matrix:
            for i in range(len(matrix[0])):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            print(heights)
            result = max(result, self.largestRectangleArea(heights))
        return result

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 单调栈 O(n)
        # 此题的本质是找到每个柱形条左边和右边最近的比自己低的矩形条，然后用宽度乘上当前柱形条的高度作为备选答案。
        # 解决此类问题的经典做法是单调栈，维护一个单调递增的栈，
            # 如果当前柱形条i的高度比栈顶要低，则栈顶元素cur出栈。出栈后，cur右边第一个比它低的柱形条就是i，
            # 左边第一个比它低的柱形条是当前栈中的top。不断出栈直到栈为空或者柱形条i不再比top低。
            # 满足上述条件之后，当前矩形条i进栈。
        # 时间复杂度
        # 每个元素最多进栈一次，出栈一次，故时间复杂度为O(n)。

        heightStack = []
        indexStack = []

        maxArea = 0

        for index, height in enumerate(heights):
            if not heightStack or height > heightStack[-1]:
                heightStack.append(height)
                indexStack.append(index)

            elif height < heightStack[-1]:
                lastIndex = 0
                while heightStack and height <= heightStack[-1]:
                    lastIndex = indexStack.pop()
                    tempArea = heightStack.pop() * (index - lastIndex)
                    if tempArea > maxArea:
                        maxArea = tempArea

                heightStack.append(height)
                indexStack.append(lastIndex)
        
        while heightStack:
            tempArea = (len(heights) - indexStack.pop()) * heightStack.pop()
            if tempArea > maxArea:
                maxArea = tempArea
        
        return maxArea
