# Winter is coming! 
# Your first job during the contest is 
# to design a standard heater with fixed warm radius to warm all the houses.
# Now, you are given positions of houses and heaters on a horizontal line, 
# find out minimum radius of heaters so that all houses could be covered by those heaters.
# So, your input will be the positions of houses and heaters seperately, 
# and your expected output will be the minimum radius standard of heaters.

# Note:
# Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be warmed.
# All the heaters follow your radius standard and the warm radius will the same.
 
# Example 1:
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, 
# and if we use the radius 1 standard, then all the houses can be warmed.
 
# Example 2:
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. 
# We need to use radius 1 standard, then all the houses can be warmed.

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # M1. 贪心 O(nlogn+mlogm)
            # 将房屋和暖气的位置分别从小到大排序。
            # 逐一枚举每个房屋，对于房屋ii，他使用暖气必定是距离他左右（如果有）最近的两个之一，
            # 由于我们已经对坐标进行了排序，所以这个过程是单调的。
            # 按照上述过程，随时更新半径的最大值r即可。
        # 时间复杂度
        # 排序的时间复杂度为O(nlogn+mlogm)，然后是线性扫描，每个位置最多被遍历一次，时间复杂度为O(n+m)，
        # 故总时间复杂度为O(nlogn+mlogm)。

        # houses.sort()
        # heaters.sort() 
        # heaters = [float('-inf')] + heaters + [float('inf')] 

        # result, i = 0, 0

        # for house in houses:
        #     while house > heaters[i+1]: 
        #         i += 1 # search to put house between heaters

        #     temp_radius = min(house - heaters[i], heaters[i+1]- house)
        #     result = max(result, temp_radius)

        # return result  

        # M2. 二分 O(max(nlogn, mlogn))
        # 还是上面的思路，我们可以用二分查找法来快速找到第一个大于等于当前house位置的数，
        # 如果这个数存在，那么我们可以算出其和house的差值，
        # 并且如果这个数不是heater的首数字，我们可以算出house和前面一个数的差值，
        # 这两个数中取较小的为cover当前house的最小半径，然后我们每次更新结果res即可。

        # heaters.sort()
        # n = len(heaters)

        # # For each house, do binary search to find min radius for heaters to cover this house
        # result = 0
        # for house in houses:
        #     lo, hi = 0, n
        #     while lo < hi: #Find right boundary, eventually lo == hi
        #         mid = (lo+hi) >> 1
        #         if heaters[mid] < house:
        #             lo = mid + 1
        #         else:
        #             hi = mid

        #     # Distance to left heater
        #     left_dis = house - heaters[hi-1] if hi > 0 else 2**63-1
        #     # Distance to right heater
        #     right_dis = heaters[hi] - house if hi < n else 2**63-1

        #     result = max(result, min(left_dis, right_dis))

        # return result
        
        # M3. 二分方法的另一种实现 调用bisect模块
        # https://docs.python.org/3/library/bisect.html#module-bisect

        import bisect
        heaters.sort()
        heaters_set = set(heaters)
        result = 0

        for house in houses:
            pos = bisect.bisect(heaters, house)
            if pos == 0:
                result = max(result, heaters[0] - house)
            elif pos == len(heaters):
                result = max(result, house - heaters[-1])
            else:
                result = max(result, min(house - heaters[pos-1], heaters[pos] - house))
        return result
