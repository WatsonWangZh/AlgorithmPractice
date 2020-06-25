# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. 
# The black pixels are connected, i.e., there is only one black region. 
# Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, 
# return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

# Example:
# Input:
# [
#   "0010",
#   "0110",
#   "0100"
# ]
# and x = 0, y = 2
# Output: 6

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """

        # M1. 线性搜索
        top = bottom = x
        left = right = y

        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == '1':
                    top = min(top, i)
                    bottom = max(bottom, i+1)
                    left = min(left, j)
                    right = max(right, j+1)
                    
        return (bottom - top) * (right - left)

        # M2. 二分搜索

    #     if not image or not image[0]:
    #         return 0
    #     leftx = self.searchx1(image, 0, x)
    #     rightx = self.searchx2(image, x, len(image)-1)
    #     topy = self.searchy1(image, 0, y)
    #     bottomy = self.searchy2(image, y, len(image[0])-1)
    #     return (rightx-leftx) * (bottomy-topy)
        
    # def searchx1(self, image, start, end):
    #     while start <= end:
    #         mid = start + end >> 1
    #         flag = 0
    #         for j in range(len(image[0])):
    #             if image[mid][j] == "1":
    #                 flag = 1
    #                 break
    #         if flag:
    #             end = mid-1
    #         else: 
    #             start = mid+1
    #     return end
    
    # def searchx2(self, image, start, end):
    #     while start <= end:
    #         mid = start + end >> 1
    #         flag = 0
    #         for j in range(len(image[0])):
    #             if image[mid][j]=="1":
    #                 flag = 1
    #                 break
    #         if flag:
    #             start = mid+1
    #         else: end = mid-1
    #     return end
    
    # def searchy1(self, image, start, end):
    #     while start <= end:
    #         mid= start + end >> 1
    #         flag = 0
    #         for j in range(len(image)):
    #             if image[j][mid]=="1":
    #                 flag = 1
    #                 break
    #         if flag:
    #             end = mid-1
    #         else: 
    #             start = mid+1
    #     return end
    
    # def searchy2(self, image, start, end):
    #     while start <= end:
    #         mid = start + end-start >> 1
    #         flag = 0
    #         for j in range(len(image)):
    #             if image[j][mid] == "1":
    #                 flag = 1
    #                 break
    #         if flag:
    #             start = mid+1
    #         else:
    #             end = mid-1
    #     return end

    # M3. BFS TODO
    #     if not image or not image[0]:
    #         return 0
            
    #     top = bottom = x
    #     left = right = y

    #     self.dfs(image, x, y)

    #     return (right - left) * (top - bottom)

    # def dfs(self, image, i, j):
    #     if i < 0 or j < 0 \
    #             or i >= len(image) or j >= len(image[0]) \
    #             or image[i][j] == '0':
    #         return

    #     image[i][j] = 0

    #     top = min(top, i)
    #     bottom = max(bottom, i+1)
    #     left = min(left, j)
    #     right = max(right, j+1)

    #     self.dfs(image, i+1, j)
    #     self.dfs(image, i-1, j) 
    #     self.dfs(image, i, j+1)
    #     self.dfs(image, i, j-1)
        