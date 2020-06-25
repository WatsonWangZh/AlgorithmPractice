# You are given an integer array nums and you have to return a new counts array. 
# The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

# Example:
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # M1. 模拟 TLE
        n = len(nums)
        res = []
        for i in range(n):
            cnt = 0
            for j in range(i, n):
               if nums[j] < nums[i]:
                cnt += 1
            res.append(cnt)
        return res

        # M2. 