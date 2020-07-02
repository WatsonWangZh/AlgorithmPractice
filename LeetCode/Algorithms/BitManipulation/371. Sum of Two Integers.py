# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = -2, b = 3
# Output: 1

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        # 位运算 O(1)
        # 用<异或>来算不带进位的和(异或：0⊕0=0，1⊕0=1，0⊕1=1，1⊕1=0)
        # 用<与>并<左移>一位来算进位
        # 递归计算无进位和 与 进位 的和，直到无需进位
        
        # set MASK and MAX_INT since python will dynamically change the precision of a integer
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF 
        while b!= 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = carry << 1
        # 修正负数结果
        return a if a < MAX_INT else ~(a ^ MASK)
