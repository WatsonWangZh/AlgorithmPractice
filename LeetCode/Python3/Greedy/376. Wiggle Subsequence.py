# A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. 
# The first difference (if one exists) may be either positive or negative. 
# A sequence with fewer than two elements is trivially a wiggle sequence.
# For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. 
# In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, 
# the first because its first two differences are positive and the second because its last difference is zero.
# Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. 
# A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, 
# leaving the remaining elements in their original order.

# Example 1:
# Input: [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.

# Example 2:
# Input: [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. 
# One is [1,17,10,13,10,16,8].

# Example 3:
# Input: [1,2,3,4,5,6,7,8,9]
# Output: 2

# Follow up:
# Can you do it in O(n) time?

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # M1. 贪心 O(n)
        # 摆动序列如果画在坐标轴上的时候，它的形式其实就是向山峰一样，把所有的山顶（极大值）和山谷（极小值）元素拿出来就是一个最优解。
        # 同一趋势内只选择一个点，可以认为选择的是最高或最低点。

        n = len(nums)
        if n < 2:
            return n
        max_len = 1
        expect = 0
        for i in range(1, len(nums)):
            # 初始上升下降均可
            if expect == 0:
                if nums[i] > nums[i-1]:
                    max_len += 1
                    expect = -1
                if nums[i] < nums[i-1]:
                    max_len += 1
                    expect = 1
            # 寻找下降点
            if expect == -1:
                if nums[i] < nums[i-1]:
                    max_len += 1
                    expect = 1
            # 寻找上升点
            elif expect == 1:
                if nums[i] > nums[i-1]:
                    max_len += 1
                    expect = -1
        return max_len

        # M2. 动态规划 O(n)
        # 使用两个数组来分别表示前i个元素且最后一个状态是上升/下降的最长摆动序列长度。
        # 状态表示：dp_up[i]代表前i个元素且最后一个状态是上升的最长摆动序列长度；dp_down[i]代表前i个元素且最后一个状态是下降的最长摆动序列长度。
        # 状态初始化：dp_up[0] = dp_down[0] = 1，代表仅有一个元素时候的情况。
        # 状态转移：
        # 如果nums[i] > nums[i - 1]，那么dp_up[i] = dp_down[i - 1] + 1，说明发生了一次由下降到上升的转折；
        # 如果nums[i] < nums[i - ]，那么dp_down[i] = dp_up[i - 1] + 1，说明发生了一次由上升到下降的转折。
        # 其余情况只要简单的和上一个状态一样即可。
        # 答案表示：max(dp_up[n - 1],dp_down[n - 1])，分别代表最后一个状态是上升还是下降的最长摆动序列。

        n = len(nums)
        if n < 2:
            return n

        dp_up = [1] * n
        dp_down = [1] * n

        for i in range(1, n):
            # 由下降到上升的转折
            if nums[i] > nums[i-1]:
                dp_up[i] = dp_down[i-1] + 1
                dp_down[i] = dp_down[i-1]
            # 由上升到下降的转折
            elif nums[i] < nums[i-1]:
                dp_down[i] = dp_up[i-1] + 1
                dp_up[i] = dp_up[i-1] 
            else:
                dp_up[i] = dp_up[i-1]
                dp_down[i] = dp_down[i-1]

        return max(dp_up[n-1], dp_down[n-1])
