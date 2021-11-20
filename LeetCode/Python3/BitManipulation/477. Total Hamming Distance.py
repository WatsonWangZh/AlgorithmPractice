# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Now your job is to find the total Hamming distance between all pairs of the given numbers.

# Example:
# Input: 4, 14, 2
# Output: 6

# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

# Note:
# Elements of the given array are in the range of 0 to 10^9
# Length of the array will not exceed 10^4.

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 按位统计 O(n)
        # 将所有数对距离的计算过程按位分离，固定第i位，统计数组中数字i位为 1 的个数 ones，则第ii位贡献的答案为 ones ∗ (n−ones)。
        # 时间复杂度
        # 枚举31个数位，每次枚举会遍历整个数组，故时间复杂度为 O(31n) 。

        cnt = 0
        n = len(nums)
        for i in range(32):
            mask = 2**i
            ones = 0
            for num in nums:
                if num & mask:
                    ones += 1
            cnt += ones * (n-ones)
        return cnt