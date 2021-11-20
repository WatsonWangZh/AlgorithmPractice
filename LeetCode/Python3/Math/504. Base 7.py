# Given an integer, return its base 7 string representation.

# Example 1:
# Input: 100
# Output: "202"
# Example 2:
# Input: -7
# Output: "-10"
# Note: The input will be in range of [-1e7, 1e7].

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Simple Version
        # if not num:
        #     return str(num)
        # flag = 1
        # if num < 0:
        #     num = - num
        #     flag = -1
        # l = []
        # while num:
        #     l.append(str(num%7))
        #     num = num / 7
        # l.reverse()
        
        # res = ''.join(l)
        # if flag == -1:
        #     res = "-" + res
        # return res

        # Library Version
        sign = '' if num >= 0 else '-'
        num = abs(num)
        res = []
        while num >= 7:
            num, res = divmod(num, 7)
            res.append(str(res))
        res.append(str(num))
        return sign + ''.join(reversed(res))
