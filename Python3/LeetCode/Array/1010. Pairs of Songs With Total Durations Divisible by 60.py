# In a list of songs, the i-th song has a duration of time[i] seconds. 
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  
# Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

# Example 1:
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

# Example 2:
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.

# Note:
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500

# Hints:
# We only need to consider each song length modulo 60.
# We can count the number of songs with (length % 60) equal to r, and store that in an array of size 60.

import collections
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # 统计频次+组合计算 O(n)
        # 统计time数组中模60的种类和每种模的频次，然后根据组合数统计他们对答案的贡献。
        # 比如 20 + 40 == 60， 那么答案就加 cnt[20] * cnt[40],
        # 因为遍历过程中会再重复计算一次 cnt[40] * cnt[20], 所以答案要除以2。
        # 同时要注意处理 0 + 0 == 0 和 30 + 30 == 60 的情况。
        # 时间复杂度分析： O(n)

        nums = [i % 60 for i in time]
        cnt = collections.Counter(nums)
        result = 0

        for key in cnt.keys():

            if key == 0 or key == 30:
                result += cnt[key] * (cnt[key] - 1)

            elif 60 - key in cnt.keys():
                result += cnt(key) * cnt[60-key]

        result //= 2
        
        return result
