# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# Example 1:
# Input: [5,7]
# Output: 4

# Example 2:
# Input: [0,1]
# Output: 0

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 找规律 位运算
        # [5, 7]里共有三个数字，分别写出它们的二进制为：
        # 101　　110　　111
        # 相与后的结果为100，仔细观察我们可以得出，最后的数是该数字范围内所有的数的左边共同的部分。
        # 发现了规律后，我们只要写代码找到左边公共的部分即可:
        # 平移m和n，每次向右移一位，直到m和n相等，记录下所有平移的次数i，然后再把m左移i位即为最终结果。

        i = 1
        while m != n:
            m >>= 1
            n >>= 1
            i <<= 1
        return m * i