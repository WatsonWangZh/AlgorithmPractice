# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537

# Constraints:
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

# Hints:
# Make an array F of length 38, and set F[0] = 0, F[1] = F[2] = 1.
# Now write a loop where you set F[n+3] = F[n] + F[n+1] + F[n+2], and return F[n].

# M1. 动态规划
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 3:
            return 1 if n else 0
        x, y, z = 0, 1, 1
        for _ in range(n-2):
            x, y, z = y, z, x + y + z
        return z

# M2. 记忆递归
# class Tri:
#     def __init__(self):
#         def helper(k):
#             if k == 0:
#                 return 0
            
#             if nums[k]:
#                 return nums[k]

#             nums[k] = helper(k - 1) + helper(k - 2) + helper(k - 3) 
#             return nums[k]
        
#         n = 38
#         self.nums = nums = [0] * n
#         nums[1] = nums[2] = 1
#         helper(n - 1)
                    
# class Solution:
#     t = Tri()
#     def tribonacci(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return self.t.nums[n]

# M3. 记忆动态规划
# class Tri:
#     def __init__(self):
#         n = 38
#         self.nums = nums = [0] * n
#         nums[1] = nums[2] = 1
#         for i in range(3, n):
#             nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]
                    
# class Solution:
#     t = Tri()
#     def tribonacci(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return self.t.nums[n]