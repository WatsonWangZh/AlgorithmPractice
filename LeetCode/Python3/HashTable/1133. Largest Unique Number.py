# Given an array of integers A, return the largest integer that only occurs once.
# If no integer occurs once, return -1.

# Example 1:
# Input: [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: 
# The maximum integer in the array is 9 but it is repeated. 
# The number 8 occurs only once, so it's the answer.

# Example 2:
# Input: [9,9,8,8]
# Output: -1
# Explanation: 
# There is no number that occurs only once.
 
# Note:
# 1 <= A.length <= 2000
# 0 <= A[i] <= 1000

# Hints:
# Find the number of occurrences of each value.
# Use an array or a hash table to do that.
# Look for the largest value with number of occurrences = 1.

import collections
class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # M1. 字典实现
        # d = {}
        # A.sort(reverse=True)
        # for i in A:
        #     if i not in d:
        #         d[i] = 1
        #     else:
        #         d[i] += 1
        # # 对照下方
        # sorted_d = sorted(d.items(), key=lambda x:x[0], reverse=True)
        # for item in sorted_d:
        #     if item[1] == 1:
        #         return item[0]
        # return -1

        # Wrong Answer: d is Not Sorted.
        # for k, v in d.items():
		# 	if v == 1:
		# 		return k
        # return -1

        # M2. 调库
        # from collections import Counter
        # A.sort(reverse = True)
        # for i in sorted(Counter(A).items(), key=lambda x:x[0], reverse=True):
        #     if i[1] == 1:
        #         return i[0]
        # return -1

        # M3. 排序过滤
        freq = collections.Counter(A)
        x = list(filter(lambda x: freq[x] == 1, A))
        return max(x) if len(x) > 0 else -1