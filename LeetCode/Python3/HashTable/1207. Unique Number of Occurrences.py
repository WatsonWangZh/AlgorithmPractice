# Given an array of integers arr, 
# write a function that returns true if and only if the number of occurrences of each value in the array is unique.

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Example 2:
# Input: arr = [1,2]
# Output: false

# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
 
# Constraints:
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

# Hints:
# Find the number of occurrences of each element in the array using a hash map.
# Iterate through the hash map and check if there is a repeated value.

from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # dict 
        # occu={}
        # for num in arr:  # 记录每个num的重现次数
        #     if num not in occu:
        #         occu[num]=1
        #     else:
        #         occu[num]+=1
        # setocc=set()
        # for occ_num in occu.values(): #比较是否互不相同
        #     if occ_num in setocc:
        #         return False
        #     else:
        #         setocc.add(occ_num)
        # return True

        # 调Counter类
        c = Counter(arr)
        if len(c.keys()) == len(set(c.values())):
            return True
        return False