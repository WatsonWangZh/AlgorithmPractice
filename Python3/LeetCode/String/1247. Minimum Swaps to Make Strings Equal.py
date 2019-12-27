# You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. 
# Your task is to make these two strings equal to each other. 
# You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].
# Return the minimum number of swaps required to make s1 and s2 equal, 
# or return -1 if it is impossible to do so.

# Example 1:
# Input: s1 = "xx", s2 = "yy"
# Output: 1
# Explanation: 
# Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

# Example 2: 
# Input: s1 = "xy", s2 = "yx"
# Output: 2
# Explanation: 
# Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
# Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
# Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", 
# cause we can only swap chars in different strings.

# Example 3:
# Input: s1 = "xx", s2 = "xy"
# Output: -1

# Example 4:
# Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
# Output: 4
 
# Constraints:
# 1 <= s1.length, s2.length <= 1000
# s1, s2 only contain 'x' or 'y'.

# Hints:
# First, ignore all the already matched positions, they don't affect the answer at all. 
# For the unmatched positions, there are three basic cases (already given in the examples):
# ("xx", "yy") => 1 swap, ("xy", "yx") => 2 swaps
# So the strategy is, apply case 1 as much as possible, 
# then apply case 2 if the last two unmatched are in this case, 
# or fall into impossible if only one pair of unmatched left. 
# This can be done via a simple math.

class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # 贪心 O(n)
        # 相等的位置不需要再进行交换。
        # 对于不相同的位置，分别统计出 'x' 对应 'y' 的数量 cnt1 和 'y' 对应 'x' 的数量 cnt2。
        # 对于 cnt1，一次交换可以减少两个不同的位置，cnt2 同理。
        # 如果 cnt1 和 cnt2 不同奇偶，则说明无法交换成功，返回 -1。
        # 如果同为奇数，则需要额外两次操作交换，同为偶数则在 3 中已经交换完毕。所以最终答案为 cnt1 / 2 + cnt2 / 2 + cnt1 % 2 + cnt2 % 2。
        # 时间复杂度
        #   仅遍历一次数组，故时间复杂度为 O(n)O(n)。
        # 空间复杂度
        #   仅需要常数的空间。

        if len(s1) != len(s2):
            return -1
        n = len(s1)
        cnt1 = cnt2 = 0
        for i in range(n):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    cnt1 += 1
                else:
                    cnt2 += 1
        if cnt1 % 2 != cnt2 % 2:
            return -1
        return cnt1 // 2 + cnt2 // 2 + cnt1 % 2 + cnt2 % 2 