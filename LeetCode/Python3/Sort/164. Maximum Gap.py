# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
# Return 0 if the array contains less than 2 elements.

# Example 1:
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
#              (3,6) or (6,9) has the maximum difference 3.

# Example 2:
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.

# Note:
# You may assume all elements in the array are non-negative integers 
# and fit in the 32-bit signed integer range.
# Try to solve it in linear time/space.

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://leetcode.wang/leetcode-164-Maximum-Gap.html
        # M1. 快速排序 O(nlgn)
        if len(nums) < 2:
            return 0
        nums.sort()
        maxGap = -1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > maxGap:
                maxGap = nums[i] - nums[i-1]
        return maxGap

        # M2. 基数排序
        if len(nums) < 2:
            return 0
		 # Convert nums list to reversed bit array list
        nums = [bin(num)[2:][::-1] for num in nums]                                 
        
        for i in range(max(map(len, nums))):
            nums0 = [x for x in nums if i >= len(x) or x[i] == '0']
            nums1 = [x for x in nums if i < len(x) and x[i] == '1']
			# it will only have two buckets (0, 1) in radix sort.
            nums = nums0 + nums1                                                                     
            
	    # convert the number back to base 10 integer. 
        nums = [int(num[::-1], 2) for num in nums]     
		# 1 pass to get the largest gap
        return max(nums[i] - nums[i - 1] for i in range(1, len(nums)))

        # M3. 桶排序 鸽笼原理
        if len(nums) < 2:
            return 0

        import math
        n = len(nums)
        # Bucket labels from 0 to n-1, and store only max/min of bucket
        # Bucket ranges are from: size = ceil((max-min)/(n-1)), left = min + i*size, (left, lower + size-1)
        buckets = [[float('inf'), -float('inf')] for _ in range(n)]
        min_n, max_n  = min(nums), max(nums)

        if min_n == max_n: # for case like [1,1,1,1]
            return 0
        # Store each value in a a bucket
        size = int(math.ceil(float(max_n-min_n) / (n-1)))
        for num in nums:
            label = (num - min_n) / size
            if num < buckets[label][0]:
                buckets[label][0] = num
            if num > buckets[label][1]:
                buckets[label][1] = num
        # Go through each bucket, and loop for max gap
        # Must be between, since bucket size is less than the minimum possible max gap(assume the worst case)
        max_gap = 0
        i = 0
        while i < len(buckets) - 1:
            curr_max = buckets[i][1]
            # Find next non-empty bucket
            for j in range(i+1, len(buckets)):
                if buckets[j][0] != float('inf'):
                    max_gap = max(buckets[j][0]-curr_max, max_gap)
                    i = j
                    break
            else:
                break
        return max_gap
            