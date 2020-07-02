# You have a total of n coins that you want to form in a staircase shape, 
# where every k-th row must have exactly k coins.
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# Example 1:
# n = 5
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# Because the 3rd row is incomplete, we return 2.

# Example 2:
# n = 8
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# Because the 4th row is incomplete, we return 3.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # M1. 蛮力求和 TLE
        if n <= 1:
            return n
        level = 1
        while sum(list(range(1, level+1))) <= n:
            level += 1
        return level - 1
            
        # M2. 模拟排列
        level = 0
        count = 0
        while count + level + 1 <= n:
            level += 1
            count += level
        return level

        rows=0
        while n > 0:
            if n > rows:
                rows += 1 
            else:
                return rows 
            n = n-rows
        return rows

        # M3. 数学推导, 一元二次方程求解公式
        return (int)((2 * n + 0.25)**0.5 - 0.5)

        # M4. 数学推导, 二分查找
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
