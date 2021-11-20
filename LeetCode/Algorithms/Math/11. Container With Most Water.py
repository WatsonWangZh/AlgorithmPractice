# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, 
# such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution(object):
    def maxArea(self, height) -> int:
        # 1. Time Limit Exceeded
        # maxArea = 0
        # for j in range(len(height)):
        #     for i in range(j):
        #         tempArea = min(height[i],height[j])*(j-i)
        #         if tempArea > maxArea:
        #             maxArea = tempArea
        # return maxArea
        
        # 2.two point method
        # Runtime: 76 ms, faster than 43.46% of Python3 online submissions 
        # maxArea, left, right = 0, 0, len(height)-1
        # while right > left :
        #     tempArea = min(height[left],height[right])*(right-left)
        #     if tempArea > maxArea:
        #         maxArea = tempArea
        #     if height[left] > height[right]:
        #         right -= 1
        #     else:
        #         left += 1
        # return maxArea
        
        # 3. Improved two point method
        # Runtime: 56 ms, faster than 94.01% of Python3 online submissions
        max_Area = 0
        left = 0
        right = len(height) - 1
        
        while right > left :
            width = right - left
            if height[right] >= height[left]:
                temp_height = height[left]
                left += 1
            else:
                temp_height = height[right]
                right -= 1
                
            temp_Area = temp_height * width
            if temp_Area > max_Area:
                max_Area = temp_Area
                
        return max_Area
