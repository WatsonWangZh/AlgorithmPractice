# Assume you have an array of length n initialized with all 0's and are given k update operations.
# Each operation is represented as a triplet: [startIndex, endIndex, inc] 
# which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
# Return the modified array after all k operations were executed.

# Example:
# Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# Output: [-2,0,3,5,3]

# Explanation:
# Initial state:
# [0,0,0,0,0]
# After applying operation [1,3,2]:
# [0,2,2,2,0]
# After applying operation [2,4,3]:
# [0,2,5,5,3]
# After applying operation [0,2,-2]:
# [-2,0,3,5,3]

# Hints:
# Thinking of using advanced data structures? You are thinking it too complicated.
# For each update operation, do you really need to update all elements between i and j?
# Update only the first and end element is sufficient.
# The optimal time complexity is O(k + n) and uses O(1) extra space.

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # M1. 蛮力 O(n*k) TLE
        res = [0 for _ in range(length)]
        for start, end, val in updates:
            for i in range(start, end+1):
                res[i] += val
        return res

        # https://leetcode.com/problems/range-addition/solution/
        # https://www.cnblogs.com/grandyang/p/5628786.html
        # M2. Range Caching
        res = [0 for _ in range(length)]
        for start, end, val in updates:
            res[start] += val
            if end + 1 < length:
                res[end+1] -= val

        for i in range(1, length):
                res[i] = res[i-1] + res[i]

        return res