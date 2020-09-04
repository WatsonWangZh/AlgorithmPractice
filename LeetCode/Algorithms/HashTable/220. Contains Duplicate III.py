# Given an array of integers, find out whether there are two distinct indices i and j in the array 
# such that the absolute difference between nums[i] and nums[j] is at most t 
# and the absolute difference between i and j is at most k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true

# Example 3:
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false

# Hints:
# Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.
# Use already existing state to evaluate next state - Like, 
# a set of k sorted numbers are only needed to be tracked. 
# When we are processing the next number in array, 
# then we can utilize the existing sorted state 
# and it is not necessary to sort next overlapping set of k numbers again.

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # M1. 滑动窗口模拟 O(nk) O(1)
        if not nums or k <= 0 or t < 0:
            return False

        # for TLE case
        if t == 0:
            return len(nums) != len(set(nums))

        for i in range(len(nums)):
            for j in range(i+1, min(i+k+1, len(nums))):
                if abs(nums[i]-nums[j]) <= t:
                    return True
        return False

        # M2. 数学推导 
        # https://blog.csdn.net/qian2729/article/details/50753127
        import collections
        if k < 1 or t < 0:
            return False
        dicts = collections.OrderedDict()

        for i in range(len(nums)):
            key = nums[i] / max(1,t)
            for m in (key - 1,key,key + 1):
                if m in dicts and abs(nums[i] - dicts[m]) <= t:
                    return True
            dicts[key] = nums[i]
            if i >= k:
                dicts.popitem(last = False)
        return False
