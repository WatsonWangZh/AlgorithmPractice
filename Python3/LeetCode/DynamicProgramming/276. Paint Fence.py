# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.

# Note:
# n and k are non-negative integers.

# Example:
# Input: n = 3, k = 2
# Output: 6
# Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:
#             post1  post2  post3      
#  -----      -----  -----  -----       
#    1         c1     c1     c2 
#    2         c1     c2     c1 
#    3         c1     c2     c2 
#    4         c2     c1     c1  
#    5         c2     c1     c2
#    6         c2     c2     c1

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # 数学方法 O(n)
        # 这道题让我们粉刷篱笆，有n个部分需要刷，有k种颜色的油漆，规定了不能有超过两个的相同颜色涂的部分，问我们总共有多少种刷法。
        # 那么我们首先来分析一下，
        # 如果n=0的话，说明没有需要刷的部分，直接返回0即可，
        # 如果n为1的话，那么有几种颜色，就有几种刷法，所以应该返回k，
        # 当n=2时，k=2时，我们可以分两种情况来统计，一种是相邻部分没有相同的，一种相同部分有相同的颜色，
        # 那么对于没有相同的，对于第一个格子，我们有k种填法，对于下一个相邻的格子，由于不能相同，所以我们只有k-1种填法。
        # 而有相同部分颜色的刷法和上一个格子的不同颜色刷法相同，因为我们下一格的颜色和之前那个格子颜色刷成一样的即可，
        # 最后总共的刷法就是把不同和相同两个刷法加起来。

        if n == 0 or k == 0 : 
            return 0
        
        same, diff = 0, k
        
        for i in range(2, n+1):
            temp = diff
            diff = (same + diff) * (k - 1)
            same = temp
            
        return same + diff