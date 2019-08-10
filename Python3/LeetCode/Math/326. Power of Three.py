# Given an integer, write a function to determine if it is a power of three.

# Example 1:
# Input: 27
# Output: true

# Example 2:
# Input: 0
# Output: false

# Example 3:
# Input: 9
# Output: true

# Example 4:
# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # M1. 常规操作
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1
        
        # M2. 数论 O(1)
        # 判断 n 是否是3的次幂，即判断 n 的质因子是否只有3。
        # 整型范围内3的最大次幂是 3^19=1162261467。则 n 的质因子只有3，就等价于 n 能整除 1162261467。
        #  时间复杂度分析：只有一次取模运算，时间复杂度是 O(1)。
        return n > 0 and 1162261467 % n == 0

        # M3. 求对数，然后乘方，判断得数是否相等
        return n > 0 and 3 ** round(math.log(n,3)) == n
        
        # M4. 对数换底公式
        return (n > 0 and int(math.log(n, 10) / math.log(3, 10)) - math.log(n, 10) / math.log(3, 10) == 0)