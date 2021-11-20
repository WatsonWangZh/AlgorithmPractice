# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:
# Input: 16
# Output: true

# Example 2:
# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?
import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # M1. 常规操作
        if num <= 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1
        
        # M2. 位运算
        # 0101 and 1000(8) = 0000
        # 0101 and 0100(4) = 0100
        return num > 0 and num & (num-1) == 0 and num & 0x555555555
        
        # M3. 数论
        # num 是4的整数次幂，等价于 num 是平方数，且 num 的质因子只有2。
        # int范围内，2的最大的整数次幂是 2^30，所以 num 的质因子只有2，等价于 umn 能整除 2^30。
        # 时间复杂度分析：只有常数次计算，所以时间复杂度是 O(1)。
        return num > 0 and math.sqrt(num) * math.sqrt(num) == num and (1 << 30) % num == 0
