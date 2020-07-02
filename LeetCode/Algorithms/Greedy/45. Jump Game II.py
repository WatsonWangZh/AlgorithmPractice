# Given an array of non-negative integers, 
# you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# Example:
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Note:
# You can assume that you can always reach the last index.

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 贪心 O(n)
        # 这是在 55 Jump Game 之上给出的问题，题目已经保证能够跳到最后。
        # 遍历数组，
        # 起始到当前坐标所有跳跃方式能够到达的最远距离是reach，
        # 我们跳n步能到达的最远距离用longest表示，
        # 如果longest不能到达当前坐标，说明就要多跳一步了，直接跳到当前坐标之前的点能够跳到的最远位置。

        length = len(nums)
        counter = 0
        longest = 0
        reach = 0

        for i in range(length):
            if longest < i:
                counter += 1
                longest = reach
            reach = max(reach, nums[i] + i)

        return counter
