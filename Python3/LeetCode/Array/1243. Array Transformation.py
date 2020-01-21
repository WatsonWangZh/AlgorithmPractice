# Given an initial array arr, every day you produce a new array using the array of the previous day.

# On the i-th day, 
# you do the following operations on the array of day i-1 to produce the array of day i:
# If an element is smaller than both its left neighbor and its right neighbor, 
# then this element is incremented.
# If an element is bigger than both its left neighbor and its right neighbor, 
# then this element is decremented.
# The first and last elements never change.
# After some days, the array does not change. Return that final array.

# Example 1:
# Input: arr = [6,2,3,4]
# Output: [6,3,3,4]
# Explanation: 
# On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
# No more operations can be done to this array.

# Example 2:
# Input: arr = [1,6,3,4,3,5]
# Output: [1,4,4,4,4,5]
# Explanation: 
# On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
# On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
# No more operations can be done to this array.
 
# Constraints:
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 100

# Hints:
# Try to simulate the process.
# For every iteration, find the new array using the old one and the given rules.

class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # 模拟 O(n) O(n)
        change = True
        while change:
            arr_back = arr[:]
            for i in range(1, len(arr_back)-1):
                if arr_back[i] > arr_back[i-1] and arr_back[i] > arr_back[i+1]:
                    arr[i] -= 1
                elif arr_back[i] < arr_back[i-1] and arr_back[i] < arr_back[i+1]:
                    arr[i] += 1
            if arr_back == arr:
                change = False
        return arr
                