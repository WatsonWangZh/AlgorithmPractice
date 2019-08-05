# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint 
# stopping you from robbing each of them is that adjacent houses have security system 
# connected and it will automatically contact the police if two adjacent houses 
# were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, 
# determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划 O(n)
        # 令rob[i]表示盗窃了第i个房间所能得到的最大收益，norob[i]表示不盗窃第i个房间所能得到的最大收益。
            # rob[i] = norob[i - 1] + nums[i]，norob[i] = max(rob[i - 1], norob[i - 1])。
        # 初始值rob[0] = nums[0], norob[0] = 0。
        # 答案为max(rob[n - 1], norob[n - 1])。
        # 时间复杂度分析: 状态数为O(n)，转移数为O(1)，转移时间为O(1)，故总时间复杂度为O(n)。

        # 原始解法
        # if not nums:
        #     return 0

        # n = len(nums)
        # rob = [0 for _ in range(n)]
        # norob = [0 for _ in range(n)]
        
        # rob[0] = nums[0]
        # norob[0] = 0

        # for i in range(1, n):
        #     rob[i] = norob[i-1] + nums[i]
        #     norob[i] = max(rob[i-1], norob[i-1])
        # return max(rob[n-1], norob[n-1])

        # 优化解法 由于每次更新只用到了上一层的信息，故可以优化空间为常数。
        if not nums:
            return 0
        
        rob = nums[0]
        norob = 0

        for i in range(1, len(nums)):
            last_rob = rob
            last_norob = norob
            rob = last_norob + nums[i]
            norob = max(last_norob, last_rob)

        return max(rob, norob)
