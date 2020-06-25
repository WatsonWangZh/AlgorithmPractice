# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
# To perform a "flood fill", consider the starting pixel, 
# plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
# plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), 
# and so on. 
# Replace the color of all of the aforementioned pixels with the newColor.
# At the end, return the modified image.

# Example 1:
# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.

# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

# Hints:
# Write a recursive function that paints the pixel if it's the correct color, then recurses on neighboring pixels.

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # M1. BFS
        # 从当前像素点(sr, sc)开始，修改颜色，并遍历四周，相同颜色则加入queue
        # 没有得加的时候，从queue中取出像素点，设置为当前像素点
        # 重复1、2，直到queue为空
        # 注意，要用一个额外的二维数组表示某个点是否进入过queue，避免重复进入。

        from collections import deque
        dy = [0, 1, 0, -1]
        dx = [1 ,0 ,-1, 0]
        h = len(image)
        w = len(image[0])
        used = [[False for i in range(w)] for j in range(h)] 
        q = deque()

        rawColor = image[sr][sc]
        image[sr][sc] = newColor
        q.append((sr, sc))
        used[sr][sc] = True

        while len(q) != 0:
        # while q is not None: not correct
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < h and 0 <= nx < w and not used[ny][nx] and image[ny][nx] == rawColor:
                    image[ny][nx] = newColor
                    used[ny][nx] = True
                    q.append((ny, nx))

        return image

        # M2. 递归DFS

        if image[sr][sc] == newColor:
            return image

        y, x = sr, sc
        h = len(image)
        w = len(image[0])
        dy = [0, 1, 0, -1]
        dx = [1 ,0 ,-1, 0]
        rawColor = image[sr][sc]
        image[sr][sc] = newColor

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and image[ny][nx] == rawColor:
                self.floodFill(image, ny, nx, newColor)

        return image