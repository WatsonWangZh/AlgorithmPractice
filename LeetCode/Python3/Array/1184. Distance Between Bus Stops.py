# A bus has n stops numbered from 0 to n - 1 that form a circle. 
# We know the distance between all pairs of neighboring stops 
# where distance[i] is the distance between the stops number i and (i + 1) % n.
# The bus goes along both directions i.e. clockwise and counterclockwise.
# Return the shortest distance between the given start and destination stops.

# Example 1:
# Input: distance = [1,2,3,4], start = 0, destination = 1
# Output: 1
# Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

# Example 2:
# Input: distance = [1,2,3,4], start = 0, destination = 2
# Output: 3
# Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

# Example 3:
# Input: distance = [1,2,3,4], start = 0, destination = 3
# Output: 4
# Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.

# Constraints:
# 1 <= n <= 10^4
# distance.length == n
# 0 <= start, destination < n
# 0 <= distance[i] <= 10^4

# Hints:
# Find the distance between the two stops if the bus moved in clockwise or counterclockwise directions.

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        # 模拟，O(n)
        # 求出环形路线的总长度tot，然后求出从start到destination的一个方向的距离，
        # 另一方向的距离可以直接用tot减去来得到。
        # 最后返回二者中较小的即可。
        
        n = len(distance)
        tot = 0
        for i in range(n):
            tot += distance[i]
        res = 0
        while start != destination:
            res += distance[start]
            start += 1
            if start == n:
                start = 0
        return min(res, tot - res)