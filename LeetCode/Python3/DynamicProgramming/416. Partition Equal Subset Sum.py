# Given a non-empty array containing only positive integers, 
# find if the array can be partitioned into two subsets 
# such that the sum of elements in both subsets is equal.

# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
 
# Example 1:
# Input: [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
 
# Example 2:
# Input: [1, 2, 3, 5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        c = nums_sum // 2
        dp = [[0] * (c+1) for _ in range(len(nums))]
        # 对第一列数据进行处理
        for i in range(len(nums)):
            dp[i][0] = 1
        # 对放进来的第一个数进行处理
        if nums[0] <= c:
            dp[0][nums[0]] = 1
        for i in range(1, len(nums)):
            num = nums[i]
            for j in range(1, c+1):
                if num > j:
                    dp[i][j] = dp[i-1][j]
                    continue
                dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
        return dp[-1][-1]

        # 空间优化一
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        c = nums_sum // 2
        dp = [[0] * (c+1) for _ in range(2)]
        # 对第一列数据进行处理
        dp[0][0], dp[1][0] = 1, 1
        # 对放进来的第一个数进行处理
        if nums[0] <= c:
            dp[0][nums[0]] = 1
        for i in range(1, len(nums)):
            num = nums[i]
            for j in range(1, c+1):
                cur = i % 2
                pre = 1 if cur == 0 else 0
                if num > j:
                    dp[cur][j] = dp[pre][j]
                    continue
                dp[cur][j] = dp[pre][j] or dp[pre][j-num]
        return dp[-1][-1]

        # 优化二
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        c = nums_sum // 2
        dp = [0] * (c+1) 
        # 对第一列数据进行处理
        dp[0] = 1
        # 对放进来的第一个数进行处理
        if nums[0] <= c:
            dp[nums[0]] = 1
        # 反向填充最后一行元素
        for i in range(1, len(nums)):
            num = nums[i]
            for j in range(c, 0, -1):
                if num > j:
                    continue
                dp[j] = dp[j] or dp[j-num]
        return dp[-1]

        # 最终版
        c = sum(nums)
        if c % 2 != 0:
            return False
        c = c // 2
        dp = [0] * (c+1)
        # 对第一列数据进行处理
        dp[0] = 1 
        # 反向填充最后一行元素
        for num in nums:
            for i in range(c, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[-1]