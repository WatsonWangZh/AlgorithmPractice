# A conveyor belt has packages that must be shipped from one port to another within D days.
# The i-th package on the conveyor belt has a weight of weights[i].  
# Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
# We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship 
# that will result in all the packages on the conveyor belt being shipped within D days.

# Example 1:
# Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# Output: 15
# Explanation: 
# A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
# Note that the cargo must be shipped in the order given, 
# so using a ship of capacity 14 and splitting the packages into parts like 
# (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 

# Example 2:
# Input: weights = [3,2,2,4,1,4], D = 3
# Output: 6
# Explanation: 
# A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4

# Example 3:
# Input: weights = [1,2,3,1,1], D = 4
# Output: 3
# Explanation: 
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
 
# Note:
# 1 <= D <= weights.length <= 50000
# 1 <= weights[i] <= 500

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        # 二分 + 模拟  O(N*log(N*M))
        # 二分枚举船的载重，载重下限是最大物品的重量。载重上限是所有物品的和。
        # 然后求中点是否满足 D 天内运输完成，如果满足则进一步降低上限，不满足就提高下限，
        # 直到找到刚好满足 D 天运输完成为止。
        # 时间复杂度分析：O(N*log(N*M))
        # 其中枚举过程复杂度O(log(weights.length() * weights[i])),模拟计算天数复杂度 O(weights.length())

        max_item = 0
        curr_item_sum = [0]
        for weight in weights:
            curr_item_sum.append(curr_item_sum[-1]+weight)
            max_item = max(max_item, weight)
        
        low_bound = max_item - 1 
        up_bound = curr_item_sum[-1] + 1
        
        while low_bound + 1 < up_bound:
            temp_capacity = (low_bound + up_bound) // 2
            day_count = 0
            i = 0
            j = 1
            while j < len(curr_item_sum):
                while j < len(curr_item_sum) and curr_item_sum[j] - curr_item_sum[i] <= temp_capacity:
                    j += 1 
                day_count += 1
                if day_count > D:
                    break
                i = j - 1
                
            if day_count > D:
                low_bound = temp_capacity
            else:
                up_bound = temp_capacity
                
        return up_bound
    