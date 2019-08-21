# You are given a string representing an attendance record for a student. 
# The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) 
# or more than two continuous 'L' (late).
# You need to return whether the student could be rewarded according to his attendance record.

# Example 1:
# Input: "PPALLP"
# Output: True

# Example 2:
# Input: "PPALLL"
# Output: False

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 模拟 O(n)
        # 直接按照题目所说，判断两种情况是否存在即可。
        # 时间复杂度
        # 仅遍历一次字符串，故时间复杂度为 O(n)。

        L = 0
        A = 0

        for item in s:
            if item == "A":
                A += 1
                L = 0
                if A > 1:
                    return False
            elif item == "L":
                L += 1
                if L > 2:
                    return False
            else:
                L = 0

        return True