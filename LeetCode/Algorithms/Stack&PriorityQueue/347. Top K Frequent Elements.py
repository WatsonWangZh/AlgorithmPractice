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

from collections import defaultdict, Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # M1.内置函数
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

        # M2.桶排序
        cnt = defaultdict(int)
        res = []
        for num in nums:
            cnt[num] += 1

        bucket = [[] for i in range(max(cnt.values()))]
        for key, value in cnt.items():
            bucket[value-1].append(key)
        
        for key, value in enumerate(bucket[::-1]):
            if len(value):
                res = res + value
            if len(res) == k:
                break

        return res

        # N3, 最小堆
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1

        q = []
        for key, value in cnt.items():
            if len(q) < k:
                heapq.heappush(q, (value, key))
            elif value > q[0][0]:
                heapq.heapreplace(q, (value, key))

        res = []
        while q:
            res.append(heapq.heappop(q)[1])

        return res
