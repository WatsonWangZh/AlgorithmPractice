# Given n non-negative integers representing the histogram's bar height 
# where the width of each bar is 1, find the area of largest rectangle in the histogram.
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# Example:
# Input: [2,1,5,6,2,3]
# Output: 10

class Solution(object):
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

