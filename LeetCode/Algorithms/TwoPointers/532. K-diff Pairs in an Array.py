# Given an array of integers and an integer k, 
# you need to find the number of unique k-diff pairs in the array. 
# Here a k-diff pair is defined as an integer pair (i, j), 
# where i and j are both numbers in the array and their absolute difference is k.

# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

# Note:
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 统计数字及频数 特判k为0的情况 O(n)
        # 统计数组中每个数字的个数,建立每个数字和其出现次数之间的映射，然后遍历哈希表中的数字，
        # 如果k为0且该数字出现的次数大于1，则结果res自增1；
        # 如果k不为0，且用当前数字加上k后得到的新数字也在原数组中存在，则结果res自增1。

        if k < 0:
            return 0
        if k == 0:
            d = {}
            for num in nums:
                if num not in d:
                    d[num] = 1
                else:
                    d[num] += 1
            res = 0
            for num in d:
                if d[num] > 1:
                    res += 1
            return res
        
        s = set(nums)
        return sum([1 if ss + k in s else 0 for ss in s])