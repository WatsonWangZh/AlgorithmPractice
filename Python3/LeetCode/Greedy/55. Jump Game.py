# Given an array of non-negative integers, 
# you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# Example 1:
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 贪心 O(n)
        # 先想一下什么时候不能够完成跳跃，在当前位置之前（包括当前位置）能够跳跃到的最远距离就是当前位置，且这时候还没有到终点；
        # 什么样的情况就能保证可以跳到终点呢，只要当前最远距离超过终点即可。
        # 只要当前的位置没有超过能跳到的最远距离，就可以不断的刷新最远距离来继续前进。

        if not nums:
            return False

        length = len(nums)
        index = 0
        longest = nums[0]

        while index <= longest:
            if longest >= length - 1:
                return True
            longest = max(longest, index + nums[index])
            index += 1
            
        return False
