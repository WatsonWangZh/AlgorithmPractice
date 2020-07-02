# In some array arr, the values were in arithmetic progression: 
# the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
# Then, a value from arr was removed that was not the first or last value in the array.
# Return the removed value.

# Example 1:
# Input: arr = [5,7,11,13]
# Output: 9
# Explanation: The previous array was [5,7,9,11,13].

# Example 2:
# Input: arr = [15,13,12]
# Output: 14
# Explanation: The previous array was [15,14,13,12].
 
# Constraints:
# 3 <= arr.length <= 1000
# 0 <= arr[i] <= 10^5

# Hints:
# Assume the sequence is increasing, what if we find the largest consecutive difference?
# Is the missing element in the middle of the segment with the largest consecutive difference?
# For decreasing sequences, just reverse the array and do a similar process.

class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # 找出差 逐个核查
        n = len(arr)
        gap = arr[n-1] - arr[0]
        inc = gap // n
        if inc == 0:
            return 0
        for i in range(len(arr)):
            if arr[i] != arr[0] + i*inc:
                return arr[0] + i*inc