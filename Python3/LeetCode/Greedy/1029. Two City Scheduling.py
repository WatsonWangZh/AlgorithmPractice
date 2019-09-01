# There are 2N people a company is planning to interview. 
# The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

# Example 1:
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 
# Note:
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # 排序贪心 O(nlogn)
        # 这道题先假设所有的人都去A市，然后我们只需要选取去B市的费用与去A市的费用的差最小的N个人改去B市即可。
        # 时间复杂度分析：排序时间复杂度O(nlogn)。

        dif = [cost[1]-cost[0] for cost in costs]

        result = sum([cost[0] for cost in costs])
        dif.sort()

        for i in range(len(costs)//2):
            result += dif[i]
            
        return result