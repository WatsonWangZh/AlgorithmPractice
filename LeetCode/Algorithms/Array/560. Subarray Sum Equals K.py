# Given an array of integers and an integer k, 
# you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2

# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

# Hints:
# Will Brute force work here? Try to optimize it.
# Can we optimize it by using some extra space?
# What about storing sum frequencies in a hash table? Will it be useful?
# sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. 
# Can we use this property to optimize it.

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 前缀和，哈希表 O(n)
        #   对原数组求前缀和后，一个和为 k 的子数组即为一对前缀和的差值为 k 的位置。
        #   遍历前缀和数组，用哈希表记录每个前缀和出现的次数。特别地，初始时前缀和为 0 需要被额外记录一次。
        #   遍历过程中，对于当前前缀和 temp，累计之前 temp - k 前缀和出现的次数累积到答案即可。
        # 时间复杂度
        #   每个位置仅遍历一次，哈希表单次操作的时间复杂度为 O(1)，故总时间复杂度为 O(n)。

        result = 0
        hash_prefixsum_freq = {} # {int:int}
        hash_prefixsum_freq[0] = 1
        
        temp =0

        for num in nums:
            temp += num
            if temp-k in hash_prefixsum_freq:
                result += hash_prefixsum_freq[temp-k]
            hash_prefixsum_freq[temp] = hash_prefixsum_freq.setdefault(temp, 0) + 1

        return result
