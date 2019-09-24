# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

# Example 1:
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 4.

# Note:
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

# Follow up:
# What if the input numbers come in one by one as an infinite stream? 
# In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. 
# Could you solve it efficiently?

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # M1. 分两段记录：初次遇到0（包含0） 和 第二次遇到0
        # res = cur = cnt = 0
        # for num in nums:
        #     cnt += 1
        #     if num == 0:
        #         cur = cnt
        #         cnt = 0
        #     res = max(res, cur + cnt)
        # return res

        # M2. 滑动窗口 
        # res = cnt_zero = left = 0
        # k = 1
        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         cnt_zero += 1
        #     while cnt_zero > k:
        #         if nums[left] == 0:
        #             cnt_zero -= 1
        #         left += 1
                
        #     res = max(res, right - left + 1)
        # return res

        # M3. 流式记录0元素位置
        res = left = 0
        k = 1 
        q = []
        for right in range(len(nums)):
            if nums[right] == 0:
                q.append(right)
            if len(q) > k:
                left = q[0] + 1
                q.pop(0)
            res = max(res, right - left + 1)
        return res