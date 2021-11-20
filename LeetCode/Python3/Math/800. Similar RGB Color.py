# In the following, every capital letter represents some hexadecimal digit from 0 to f.
# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  
# For example, "#15c" is shorthand for the color "#1155cc".
# Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" 
# is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
# Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, 
# and has a shorthand (that is, it can be represented as some "#XYZ"

# Example 1:
# Input: color = "#09f166"
# Output: "#11ee66"
# Explanation:  
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
# This is the highest among any shorthand color.

# Note:
# color is a string of length 7.
# color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
# Any answer which has the same (highest) similarity as the best answer will be accepted.
# All inputs and outputs should use lowercase letters, and the output is 7 characters.

class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        # M1. 蛮力算法 依题意枚举检查 O(16^3)=O(1)
        # tr, tg, tb = (int(color[x:x+2], 16) for x in (1,3,5))
        # res = ()
        # delta = float('inf')
        # for r in range(16):
        #     for g in range(16):
        #         for b in range(16):
        #             tmp_delta = sum((ic - c*17)**2 for ic, c in zip((tr,tg,tb),(r,g,b)))
        #             if tmp_delta < delta:
        #                 delta = tmp_delta
        #                 res = r, g, b
        # return '#' + ''.join(hex(c)[2]*2 for c in res)

        # M2. 数学分析 缩小搜索空间 取余取模
        # Because color similarity is a sum of the similarity of individual color components, 
        # we can treat each colored component separately and combine the answer.
        # https://www.cnblogs.com/grandyang/p/9296602.html

        def rounding(comp):
            q, r = divmod(int(comp, 16), 17)
            if r > 8: q += 1
            return '{:02x}'.format(17 * q)

        return '#' + rounding(color[1:3]) + rounding(color[3:5]) + rounding(color[5:])