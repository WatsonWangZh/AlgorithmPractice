# Given an array A of integers and integer K, 
# return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. 
# If no i, j exist satisfying this equation, return -1.

# Example 1:
# Input: A = [34,23,1,24,75,33,54,8], K = 60
# Output: 58
# Explanation: 
# We can use 34 and 24 to sum 58 which is less than 60.

# Example 2:
# Input: A = [10,20,30], K = 15
# Output: -1
# Explanation: 
# In this case it's not possible to get a pair sum less that 15.
 
# Note:
# 1 <= A.length <= 100
# 1 <= A[i] <= 1000
# 1 <= K <= 2000

# Hints:
# What if we have the array sorted?
# Loop the array and get the value A[i] then we need to find a value A[j] such that A[i] + A[j] < K which means A[j] < K - A[i]. 
# In order to do that we can find that value with a binary search.

class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # 双指针 O(nlgn)
        A.sort()
        if K <= A[0]:
            return -1

        left, right = 0, len(A) - 1
        res = 0
        while left < right:
            if A[left]+ A[right] < K:
                res = max(res,A[left]+ A[right])
                left += 1
            else:
                right -= 1
        return res if res > 0 else -1
