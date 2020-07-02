# Given a picture consisting of black and white pixels, find the number of black lonely pixels.
# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.
# A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

# Example:
# Input: 
# [['W', 'W', 'B'],
#  ['W', 'B', 'W'],
#  ['B', 'W', 'W']]
# Output: 3
# Explanation: All the three 'B's are black lonely pixels.

# Note:
# The range of width and height of the input 2D array is [1,500].

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        # 两次遍历，第一次将各行各列的黑像素的个数都统计出来，
        # 然后再扫描所有的黑像素一次，看其是否是该行该列唯一的存在，是的话就累加计数器。
        
        if not picture or not picture[0]:
            return 0
        m, n = len(picture), len(picture[0])
        res = 0
        rowCnt, colCnt = [0 for i in range(m)], [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    rowCnt[i] += 1
                    colCnt[j] += 1
        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    if rowCnt[i] == 1 and colCnt[j] == 1:
                        res += 1
        return res