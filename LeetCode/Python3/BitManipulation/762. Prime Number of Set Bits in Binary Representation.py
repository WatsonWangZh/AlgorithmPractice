# Given two integers L and R, 
# find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.
# (Recall that the number of set bits an integer has is the number of 1s present when written in binary. 
# For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

# Example 1:
# Input: L = 6, R = 10
# Output: 4
# Explanation:
# 6 -> 110 (2 set bits, 2 is prime)
# 7 -> 111 (3 set bits, 3 is prime)
# 9 -> 1001 (2 set bits , 2 is prime)
# 10->1010 (2 set bits , 2 is prime)

# Example 2:
# Input: L = 10, R = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)

# Note:
# L, R will be integers L <= R in the range [1, 10^6].
# R - L will be at most 10000.

# Hints:
# Write a helper function to count the number of set bits in a number, 
# then check whether the number of set bits is 2, 3, 5, 7, 11, 13, 17 or 19.

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # 枚举 位运算 O(n)
        # 由于区间[L, R]中最多只有10000个数，所以我们可以直接枚举区间中的每个数，然后统计出二进制表示中1个数s，再判断s是否是质数即可。
        # 由于L, R均不大于1000000，所以其二进制表示最多有20位，我们可以预先将20以内的所有质数都存到哈希表中，然后就可以 O(1) 判断s是否是质数了。
        # 另外这里有个常用技巧：
        # 判断整数x的第k位是否是1，可以使用位运算来做：x >> k & 1。
        # 时间复杂度分析：总共需要枚举 n 个数，每个数最多枚举20位二进制位，所以总计算量是 20n，时间复杂度是 O(n)。
        
        res = 0
        prime = [2, 3, 5, 7, 11, 13, 17]
        for num in range(L, R + 1):
            set_bits_cnt = 0
            while num != 0:
                if num & 1 == 1:
                    set_bits_cnt += 1
                num = num >> 1
            if set_bits_cnt in prime:
                res += 1
        return res
