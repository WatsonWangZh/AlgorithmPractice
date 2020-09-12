# Find all possible combinations of k numbers that add up to a number n, 
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        tmp = []

        def dfs(start, n, k):
            if not n:
                if not k:
                    res.append(tmp[:])
            elif k:
                for i in range(start, 10):
                    if n >= i:
                        tmp.append(i)
                        dfs(i + 1, n - i, k - 1)
                        tmp.pop()

        dfs(1, n, k)
        return res
