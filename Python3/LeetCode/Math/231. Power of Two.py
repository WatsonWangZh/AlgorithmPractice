# Given an integer, write a function to determine if it is a power of two.

# Example 1:
# Input: 1
# Output: true 
# Explanation: 2^0 = 1

# Example 2:
# Input: 16
# Output: true
# Explanation: 2^4 = 16

# Example 3:
# Input: 218
# Output: false

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # M1. 常规操作
        # if n <= 0:
        #     return False
        # while n % 2 == 0:
        #     n /= 2
        # return n == 1
        
        # 位运算 O(1)
        # 如果 n <= 0 则显然是 false；否则，有如下两种做法（不限于这两种）：
        # 方法 1：判断 (n & (-n)) == n ，取负运算是将 n 的二进制位取反然后再加 1。
            # 这种运算有个名称叫 lowbit，即取出 n 二进制位中从低位数第一个 1 的位置 k ，并返回 2^k。
            # 判断 (n & (-n)) == n 成立即意味着 n 二进制位中从低位数第一个 1 的位置就是最高位。
        # 方法 2：判断 n & (n - 1) == 0 ，
        #   若成立，则显然 n 只有最高的二进制位是 1，后续的二进制位都是 0，符合 2 的幂次。
        # M2.
        # return n > 0 and n & (n-1) == 0
    
        # M3.
        return n > 0 and n & (-n) == n
    