# Given a list of non negative integers, arrange them such that they form the largest number.

# Example 1:
# Input: [10,2]
# Output: "210"

# Example 2:
# Input: [3,30,34,5,9]
# Output: "9534330"

# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # https://www.cnblogs.com/grandyang/p/4225047.html
        # M1. 自定义排序 
        nums = [str(num) for num in nums]
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y)) # Trick
        # for case 
        # Input:[0,0]
        # Output:"00"
        # Expected:"0"
        return ''.join(nums) if nums and nums[0]!='0' else '0'

        # M2. 自定义排序
        nums = [str(num) for num in nums]
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y)) # Trick
        # for case 
        # Input:[0,0]
        # Output:"00"
        # Expected:"0"
        return ''.join(nums).lstrip('0') or '0'

        