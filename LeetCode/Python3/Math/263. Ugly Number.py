# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Example 1:
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3

# Example 2:
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2

# Example 3:
# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.
# Note:

# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # 将这个正整数不断除以2、3、5这三个质数直到不能继续整除2、3、5为止，
        # 如果这个数是“丑数”，那么最后会剩下1，
        # 否则如果这个数质因数还包含2、3、5以外的质数，那么最后会剩下其他的质因数，
        # 所以通过判断最后剩下的值是不是1即可判断该数是否为“丑数”。
        # 注意题目给出了输入范围为[−2^31,2^31−1]，说明在int型范围内，
        # 并且注意“丑数”必须为正整数，当输入不是正整数则直接返回false即可。
        # 时间复杂度分析：需要除以log(n)次的2、3和5，所以复杂度为O(log(n))。

        if num <= 0:
            return False
        
        for x in [2,3,5]:
            while num %x == 0:
                num /= x
                
        return num == 1