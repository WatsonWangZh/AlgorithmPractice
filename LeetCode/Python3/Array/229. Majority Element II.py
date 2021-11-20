# Given an integer array of size n, 
# find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:
# Input: [3,2,3]
# Output: [3]

# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Moore Voting Algorithm, 
        # there cannot be more than 2 values that have count larger than n/3, counting on 2 keys.
        if not nums:
            return []
        candidate1, counter1 = 0, 0
        candidate2, counter2 = 1, 0
        # Pass-1: Find the potential candidates
        for num in nums:
            if num == candidate1:
                counter1 += 1
            elif num == candidate2:
                counter2 += 1
            elif counter1 == 0:
                candidate1 = num
                counter1 = 1
            elif counter2 == 0:
                candidate2 = num
                counter2 = 1
            else:
                counter1 -= 1
                counter2 -= 1
        # Pass-2: Confirm the identified candidates
        counter1 = counter2 = 0
        res = []
        for num in nums:
            if num == candidate1:
                counter1 += 1
            if num == candidate2:
                counter2 += 1
        if counter1 > len(nums)//3:
            res.append(candidate1)
        if counter2 > len(nums)//3:
            res.append(candidate2)
        return res