# Given m arrays, and each array is sorted in ascending order. 
# Now you can pick up two integers from two different arrays (each array picks one) 
# and calculate the distance. We define the distance between two integers a and b 
# to be their absolute difference |a-b|. Your task is to find the maximum distance.

# Example 1:
# Input: 
# [[1,2,3],
#  [4,5],
#  [1,2,3]]
# Output: 4

# Explanation: 
# One way to reach the maximum distance 4 is to pick 1 in the first or third array 
# and pick 5 in the second array.

# Note:
# Each given array will have at least 1 number. There will be at least two non-empty arrays.
# The total number of the integers in all the m arrays will be in the range of [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].

import heapq
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # 双堆实现，分别保存最小值和最大值 O(n)
        max_heap, min_heap = [], []
        for i in range(len(arrays)):
            heapq.heappush(min_heap, (arrays[i][0], i))
            heapq.heappush(max_heap, (-arrays[i][-1], i))

        res = 0
        max_ele = heapq.heappop(max_heap)
        min_ele = heapq.heappop(min_heap)
        if max_ele[1] != min_ele[1]:
            return -max_ele[0] - min_ele[0]
        else:
            return max(-max_ele[0] - heapq.heappop(min_heap)[0], 
                       -heapq.heappop(max_heap)[0] - min_ele[0])