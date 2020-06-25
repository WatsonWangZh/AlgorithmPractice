# Initially on a notepad only one character 'A' is present. 
# You can perform two operations on this notepad for each step:
# Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given a number n. 
# You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. 
# Output the minimum number of steps to get n 'A'.

# Example 1:
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
 
# Note:
# The n will be in the range [1, 1000].

#Hints:
# How many characters may be there in the clipboard at the last step if n = 3? n = 7? n = 10? n = 24?

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        # DP O(n)
        dp = [i for i in range(n+1)]
        dp[1] = 0
        for i in range(2, n+1):
            for j in range(2, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        return dp[-1]

        # 递归
        if n == 1:
            return 0
        res = n
        for i in range(2, n):
            if n % i == 0:
                res = min(res, self.minSteps(i) + n/i)
        return res

        # M3. 数学 质因子的和 
        res = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                n /= factor
                res += factor
            factor += 1
        return res