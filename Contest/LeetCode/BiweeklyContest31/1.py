# 1523. Count Odd Numbers in an Interval Range
# User Accepted:4747
# User Tried:4888
# Total Accepted:4899
# Total Submissions:9570
# Difficulty:Easy
# Given two non-negative integers low and high. 
# Return the count of odd numbers between low and high (inclusive).

# Example 1:
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

# Example 2:
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
 
# Constraints:
# 0 <= low <= high <= 10^9

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        cnt = 0
        if low % 2 and high % 2:
            cnt = 2 + (high-low-2) // 2
        elif high % 2 or low % 2:
            cnt += (high-low-1) // 2 + 1
        else:
            cnt = (high-low) // 2
        return cnt
