# Numbers can be regarded as product of its factors. For example,
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.

# Note:
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.

# Example 1:
# Input: 1
# Output: []

# Example 2:
# Input: 37
# Output:[]

# Example 3:
# Input: 12
# Output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]

# Example 4:
# Input: 32
# Output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]

class Solution(object):

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 由于题目中说明了1和n本身不能算其因子，
        # 那么我们可以从2开始遍历到n，如果当前的数i可以被n整除，说明i是n的一个因子，我们将其存入一位数组tmpRes中，
        # 然后递归调用n/i，此时不从2开始遍历，而是从i遍历到n/i，停止的条件是当n等于1时，
        # 如果此时tmpRes中有因子，我们将这个组合存入结果res中。
        
        self.res = []
        if n <= 1:
            return []
        
        def dfs(num, current, currentnum, n):
            if current:
                self.res += [current + [num]]
            for i in range(currentnum,int(num**0.5)+1):
                if num % i == 0:
                    dfs(num/i, current+[i], i, n)
                    
        dfs(n, [], 2, n)
        return self.res
