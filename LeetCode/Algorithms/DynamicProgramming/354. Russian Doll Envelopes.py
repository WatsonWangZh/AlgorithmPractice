# You have a number of envelopes 
# with widths and heights given as a pair of integers (w, h). 
# One envelope can fit into another if and only if both the width and height 
# of one envelope is greater than the width and height of the other envelope.
# What is the maximum number of envelopes can you Russian doll? (put one inside other)

# Note:
# Rotation is not allowed.

# Example:
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3 
# Explanation: The maximum number of envelopes you can Russian doll is 3 
# ([2,3] => [5,4] => [6,7]).

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # 动态规划 O(n^2) 
        # 先将所有信封按宽的长度从小到大排序，
        # 然后问题变成从左到右找一条最长的h严格单调递增的子序列，同时满足w也是严格单调递增的。
        # 类似于最长上升序列问题，可以用动态规划解决。
        # 状态表示：f[i] 表示以第 i 个信封为结尾的单调序列的最大长度。
        # 状态转移：对于 f[i]，枚举 j=0∼i−1，如果第 j 个信封的长和宽都小于第 i 个信封，
        # 则用 f[j]+1 更新 f[i]。
        # 时间复杂度分析：
        # 排序部分的时间复杂度是 O(nlogn)。
        # 动态规划部分一共有 n 个状态，每个状态进行转移的计算量是 O(n)，
        # 所以动态规划的时间复杂度是 O(n^2)。
        # 总时间复杂度是 O(n^2+nlogn)=O(n^2)。

        # Time Limit Exceeded
        # if not envelopes:
        #     return 0

        # n = len(envelopes)
        # envelopes.sort(key = lambda x:(x[0], x[1]))
        # dp = [1] * n
        # for i in range(1, n):
        #     for j in range(i):
        #         if envelopes[i][0] >= envelopes[j][0] and envelopes[i][1] >= envelopes[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # 改进，二维的LIS，O(nlogn)。
        import bisect

        sortedByWidth = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        liss, l = [0] * len(envelopes), 0

        for e in sortedByWidth:
            h = e[1]
            index = bisect.bisect_left(liss, h, 0, l)
            liss[index] = h
            if index == l:
                l += 1

        return l
