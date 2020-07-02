# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.

# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped. 
# Thanks Marcos for contributing this image!

# Example:
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #  M1. 三次线性扫描 O(n)
        # 观察整个图形，想办法分解计算水的面积。
        # 注意到，每个矩形条上方所能接受的水的高度，是由它左边最高的矩形，和右边最高的矩形决定的。
        # 具体地，假设第 i 个矩形条的高度为 height[i]，
        # 且矩形条左边最高的矩形条的高度为 left_max[i]，右边最高的矩形条高度为 right_max[i]，
        # 则该矩形条上方能接受水的高度为 min(left_max[i], right_max[i]) - height[i]。
        # 需要分别从左向右扫描求 left_max，从右向左求 right_max，最后统计答案即可。

        # if not height:
        #     return 0 

        # left_max = [0 for _ in range(len(height))]
        # left_max[0] = height[0]
        # for i in range(1, len(height)):
        #     left_max[i] = max(height[i], left_max[i-1])
        
        # right_max = [0 for _ in range(len(height))]
        # right_max[-1] = height[-1]
        # for j in range(len(height)-2, -1, -1):
        #     right_max[j] = max(height[j], right_max[j+1])

        # result = 0
        # for i in range(1, len(height)-1):
        #     result += min(left_max[i], right_max[i]) - height[i]

        # return result

        # M2. 双指针 O(n)
        # https://www.bilibili.com/video/av18241289/

        left_index = 0 
        right_index = len(height) - 1
        left_max, right_max = 0, 0
        result = 0
        while left_index < right_index:
            if height[left_index] < height[right_index]:
                if height[left_index] >= left_max:
                    left_max = height[left_index]
                else:
                    result += left_max - height[left_index]
            else:
                if height[right_index] >= right_max:
                    right_max = height[right_index]
                else:
                    result += right_max - height[right_index]
        return result
            