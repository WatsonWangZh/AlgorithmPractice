# Given a year Y and a month M, return how many days there are in that month.

# Example 1:
# Input: Y = 1992, M = 7
# Output: 31

# Example 2:
# Input: Y = 2000, M = 2
# Output: 29

# Example 3:
# Input: Y = 1900, M = 2
# Output: 28
 
# Note:
# 1583 <= Y <= 2100
# 1 <= M <= 12

# Hints:
# Does February have 28 days or 29 days?
# Think of Leap years.

class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        d = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if (Y % 400 == 0 and M == 2) or (Y % 4 == 0 and Y % 100 != 0 and M == 2):
			return d[M] + 1
        else:
			return d[M]