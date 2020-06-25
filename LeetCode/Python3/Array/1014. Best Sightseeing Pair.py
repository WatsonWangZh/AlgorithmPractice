# Given an array A of positive integers, 
# A[i] represents the value of the i-th sightseeing spot, 
# and two sightseeing spots i and j have distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : 
# the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.

# Example 1:
# Input: [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 
# Note:
# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000

# Hints:
# Can you tell the best sightseeing spot in one pass (ie. as you iterate over the input?) 
# What should we store or keep track of as we iterate to do this?

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 线性扫描 O(n)
        # A[i] + A[j] + i - j 可以表示为 (A[i] + i) + (A[j] - j)，
        # 故我们需要按正序维护一个 A[i] + i 的前缀最大值，
        # 然后逆序求 (A[i] + i) + (A[j] - j) 的最大值。
        # 求的过程中，维护 A[j] - j 的后缀最大值即可。
        # 时间复杂度
        # 正反扫两遍数组，故时间复杂度为 O(n)。
        # 空间复杂度
        # 需要额外的 O(n) 的空间存储每个位置的前缀最大值。

        max_forward = [ 0 for i in range(len(A))]
        max_forward[0] = A[0]

        for i in range(1, len(A)):
            max_forward[i] = max(max_forward[i-1], A[i] + i)

        max_backward = A[len(A) - 1] - len(A) + 1
        
        result = max_forward[len(A)-2] + max_backward

        for j in range(len(A)-2, 0, -1):
            max_backward = max(max_backward, A[j] - j)
            result = max(result, max_forward[j-1] + max_backward)

        return result
