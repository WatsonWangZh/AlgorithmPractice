# Given an integer array sorted in non-decreasing order, 
# there is exactly one integer in the array that occurs more than 25% of the time.
# Return that integer.

# Example 1:
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6

# # Hints:
# Divide the array in four parts [1 - 25%] [25 - 50 %] [50 - 75 %] [75% - 100%].
# The answer should be in one of the ends of the intervals.
# In order to check which is element is the answer we can count the frequency with binarySearch.

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # 模拟
        n = len(arr)
        gap = n // 4
        for i in range(n):
            if arr[i] == arr[i+gap]:
                return arr[i]