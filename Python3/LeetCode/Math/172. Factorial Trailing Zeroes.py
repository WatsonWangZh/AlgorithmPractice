# Given an integer n, return the number of trailing zeroes in n!.

# Example 1:
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

# Example 2:
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Note: Your solution should be in logarithmic time complexity.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 质数分解 O(logn)
        # 由于n!的后缀0是由起质因子2和质因子5相乘而来的，而2的个数总是比5多的，因此我们只需要计算n!中质因子5的个数即可。
        # 要求n!中质因子5的个数即可，可以通过求∑n5i而得。
        # 例如，求245！末尾0的个数时，
            # 245/5=49 代表着有49个数(可被5整除)贡献了1个5，
            # 245/25=9 代表着有9个数(可被5×55整除)在上一行的基础上多贡献了1个5，
            # 245/125=1 代表着有1个数(可被5×5×5整除)在上一行的基础上多贡献了1个5，
            # 像数字50在第一行被call过，在第二行也被call过，给target贡献了两个5，
        # 所以245!末尾0的个数为49+9+1=59。
        # 复杂度分析：
        # 找一次5i需要O(1)时间和O(1)空间，一共需要找log5n次，所以时间复杂度是O(logn)，空间复杂度是O(logn)。

        # M1.
        res = 0
        while n:
            res += n/5
            n/=5
        return res
        
        # M2.
        return 0 if n < 5 else n / 5 + self.trailingZeroes(n/5)
        