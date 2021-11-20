# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
# You begin the journey with an empty tank at one of the gas stations.
# Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
# otherwise return -1.

# Note:
# If there exists a solution, it is guaranteed to be unique.
# Both input arrays are non-empty and have the same length.
# Each element in the input arrays is a non-negative integer.

# Example 1:
# Input: 
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.

# Example 2:
# Input: 
# gas  = [2,3,4]
# cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 贪心，双指针移动 O(n)
        # 首先用 gas - cost 求出每一段的真正花费 diff,
        # 定义两个指针start和end，分别表示当前假设的起点，和在这个起点下能走到的终点, 并选择一个合适的起点now。
        # 如果发现不能走到end，需要不断往前移动start，使得now能满足要求。
        # 如果end == start ，即找到了一个环形路线，返回start即可。
        # 时间复杂度分析:
        # 一共 n 个位置，每个位置最多遍历两次，故时间复杂度为O(n)。

        diff = [gas[i]-cost[i] for i in range(len(gas))]
        for i in range(len(diff)):
            if diff[i]>=0:
                break
            else:
                return -1

        start, end = i, (i+1)%len(diff)
        now = diff[i]

        while True:
            while now >= -diff[end]:
                now += diff[end]
                end = (end+1) % len(diff)
                if end == start:
                    return start

            while now < -diff[end]:
                start = (start-1) % len(diff)
                now += diff[start]
                if start == end:
                    return -1
                    