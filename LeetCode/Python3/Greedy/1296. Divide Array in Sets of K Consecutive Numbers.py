# Given an array of integers nums and a positive integer k, 
# find whether it's possible to divide this array into sets of k consecutive numbers
# Return True if its possible otherwise return False.

# Example 1:
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].

# Example 2:
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].

# Example 3:
# Input: nums = [3,3,2,2,1,1], k = 3
# Output: true

# Example 4:
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.
 
# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= nums.length

# Hints:
# If the smallest number in the possible-to-split array is V, 
# then numbers V+1, V+2, ... V+k-1 must contain there as well.
# You can iteratively find k sets and remove them from array until it becomes empty.
# Failure to do so would mean that array is unsplittable.

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 排序 哈希模拟 O(nlogn) O(n)
        if len(nums) % k:
            return False

        nums.sort()
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        for num in nums:
            if counter[num]:
                for i in range(num, num+k):
                    if i not in counter or counter[i] == 0 :
                        return False
                    counter[i] -= 1
        return True
