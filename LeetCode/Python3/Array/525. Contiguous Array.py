# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Note: The length of the given binary array will not exceed 50,000.

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 前缀和，哈希表 O(n)
        #  *将数组中的 0 视作 -1，则求连续相同 0 和 1 个数的子数组就是求连续和为 0 的子数组。
        #   连续子数组的和可以用两个前缀和相减得到，故这里就是求下标差距最大的两个相等的前缀和。
        #   使用哈希表记录前缀和及其下标。遍历时，若当前的前缀和在哈希表中出现，则更新答案；否则将其值和下标加入哈希表。
        #   注意哈希表中需要初始化一个前缀和 0。
        # 时间复杂度
        #   每个数字仅遍历一次，哈希表的单次操作时间复杂度为 O(1)，故总时间复杂度为 O(n)。
        # 空间复杂度
        #   需要额外的哈希表空间，故空间复杂度为 O(n)。

        n = len(nums)
        hash_table = {} # key: 前缀和（int）；  value：最前面的位置索引
        hash_table[0] = -1  # 初始化记录 前缀和-最早出现位置 哈希表

        temp = 0 #初始化前缀和
        result = 0 #初始化答案

        for i in range(n):
            if nums[i] == 1:
                temp += 1
            else:
                temp -= 1
            if temp in hash_table:
                result = max(result, i - hash_table[temp]) #注意：这里需不需要在前缀和相减的位置再加1？
            else:
                hash_table[temp] = i
                
        return result
