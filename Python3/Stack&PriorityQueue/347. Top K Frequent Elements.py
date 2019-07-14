# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), 
# where n is the array's size.
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # M1.调包 hash
        # count = collections.Counter(nums)   
        # return heapq.nlargest(k, count.keys(), key=count.get)

        # M2.手写桶排序
        cnt, res = collections.defaultdict(int), []
        for i in nums:
            cnt[i] += 1

        bucket = [[] for i in range(max(cnt.values()))]
        for key, value in cnt.items():
            bucket[value-1].append(key)
        
        for key,value  in enumerate(bucket[::-1]):
            if len(value):
                res = res + value
            if len(res) == k:
                break

        return res
            
