# There are a row of n houses, each house can be painted with one of the k colors. 
# The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by a n x k cost matrix. 
# For example, 
# costs[0][0] is the cost of painting house 0 with color 0; 
# costs[1][2] is the cost of painting house 1 with color 2, 
# and so on... Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# Example:
# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
#              Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 

# Follow up:
# Could you solve it in O(nk) runtime?

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # 动态规划 O(nk)
        # 这道题是之前那道Paint House的拓展，那道题只让用红绿蓝三种颜色来粉刷房子，
        # 而这道题让我们用k种颜色，这道题不能用之前那题的解法，会TLE。
        # 这题的解法的思路还是用DP，但是在找不同颜色的最小值不是遍历所有不同颜色，
        # 而是用min1和min2来记录之前房子的最小和第二小的花费的颜色，
        # 如果当前房子颜色和min1相同，那么我们用min2对应的值计算，
        # 反之我们用min1对应的值，这种解法实际上也包含了求次小值的方法，感觉也是一种很棒的解题思路。

        if not costs or not costs[0]: 
            return 0

        prev_min = 0
        prev_ind = -1
        prev_2min = 0

        for i in range(len(costs)):
            f_min, ind, s_min = float("inf"), -1, float("inf")
            for j in range(len(costs[i])):

                temp = costs[i][j] + (prev_min if prev_ind != j else prev_2min)

                if temp < f_min:
                    s_min = f_min
                    f_min = temp
                    ind = j
                    
                elif temp < s_min:
                    s_min = temp

            prev_min, prev_ind, prev_2min = f_min, ind, s_min
        
        return prev_min