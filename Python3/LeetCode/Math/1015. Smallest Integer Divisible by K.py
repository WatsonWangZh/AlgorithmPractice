# Given a positive integer K, 
# you need find the smallest positive integer N such that N is divisible by K, 
# and N only contains the digit 1.
# Return the length of N.  If there is no such N, return -1.

# Example 1:
# Input: 1
# Output: 1
# Explanation: The smallest answer is N = 1, which has length 1.

# Example 2:
# Input: 2
# Output: -1
# Explanation: There is no such positive integer N divisible by 2.

# Example 3:
# Input: 3
# Output: 3
# Explanation: The smallest answer is N = 111, which has length 3.
 
# Note:
# 1 <= K <= 10^5

# Hints:
# 11111 = 1111 * 10 + 1 We only need to store remainders modulo K.
# If we never get a remainder of 0, why would that happen, and how would we know that?

class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        # 暴力枚举 O(K)
        # 从 1 开始枚举 N 的长度，在枚举过程中，每次添加一个 1 之后，重新计算出当前的余数 c，
        # 之后再继续用 c 乘 10 加 1 继续尝试。
        # 如果枚举过程中 c 重复出现，则说明答案不存在。如果 c 为 0，则说明找到了可以被 K 整除的数字。
        # 时间复杂度
        # 最多遍历 K 个余数，故最多枚举 K 次就知道答案存在或者不存在，时间复杂度为 O(K)。
        # 空间复杂度
        # 需要记录余数是否出现过，故空间复杂度为 O(K)。

        if K == 1:
            return 1 

        remainder = [False for _ in range(K)]
        curr = result = 1

        while True:
            curr = (curr * 10 + 1) % K 
            result += 1 
            if curr == 0:
                return result
            elif remainder[curr]:
                break
            remainder[curr] = True

        return -1
