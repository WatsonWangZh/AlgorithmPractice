# Given an array of n integers nums and a target, 
# find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition 
# nums[i] + nums[j] + nums[k] < target.

# Example:
# Input: nums = [-2,0,1,3], and target = 2
# Output: 2 

# Explanation: Because there are two triplets which sums are less than 2:
#              [-2,0,1]
#              [-2,0,3]

# Follow up: Could you solve it in O(n^2) runtime?

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # M1. 暴力穷举法 O(n^3)

        # res = 0
        # nums.sort()
        # n = len(nums)

        # for i in range(n-2):
        #     remain = target - nums[i]
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             if nums[j] + nums[k] < remain:
        #                 res += 1

        # return res

        # M2. 双指针法 O(n^2)
        # trick: 判断三个数之和小于目标值时，此时结果应该加上right-left，以为数组排序了以后，
        # 如果加上num[right]小于目标值的话，那么加上一个更小的数必定也会小于目标值，
        # 然后我们将左指针右移一位，否则我们将右指针左移一位。

        res = 0
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            remain = target - nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] >= remain:
                    k -= 1
                else:
                    res += k - j
                    j += 1

        return res