# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, 
# return the day number of the year.

# Example 1:
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.

# Example 2:
# Input: date = "2019-02-10"
# Output: 41

# Example 3:
# Input: date = "2003-03-01"
# Output: 60

# Example 4:
# Input: date = "2004-03-01"
# Output: 61
 
# Constraints:
# date.length == 10
# date[4] == date[7] == '-', and all other date[i]'s are digits
# date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.

# Hints:
# Have a integer array of how many days there are per month. 
# February gets one extra day if its a leap year. 
# Then, we can manually count the ordinal as day + (number of days in months before this one).

class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        # 分段处理 特判闰年
        month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y = m = d = 0
        for  i in range(4):
            y = y * 10 + int(date[i])

        for i in range(5, 7):
            m = m * 10 + int(date[i])

        for i in range(8, 10):
            d = d * 10 + int(date[i])

        res = 0
        for i in range(1, m):
            res += month[i]

        res += d

        if (m > 2 and (y % 4 == 0 and y % 100 != 0 or y % 400 == 0)):
            res += 1

        return res