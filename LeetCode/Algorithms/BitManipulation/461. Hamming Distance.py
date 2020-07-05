# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.
# Note:
# 0 ≤ x, y < 2^31.

# Example:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Built-in BitCounting Functions
        return bin(x^y).count('1')

        # Bit Shift
        xor = x ^ y
        distance = 0
        while xor:
            # mask out the rest bits
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance

        # Brian Kernighan's Algorithm
        # x^(x-1) -> remove the rightmost bit of '1' in x
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance