# Given a date, return the corresponding day of the week for that date.
# The input is given as three integers representing the day, month and year respectively.
# Return the answer as one of the following values 
# {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

# Example 1:
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"

# Example 2:
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"

# Example 3:
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
 
# Constraints:
# The given dates are valid dates between the years 1971 and 2100.

# Hints:
# Sum up the number of days for the years before the given year.
# Handle the case of a leap year.
# Find the number of days for each month of the given year.

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        # 从最初开始累计到今日 查表返回
        week = [0, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        # 注意形参同名问题，大坑
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d, w = 1971, 1, 1, 5
        
        while y != year or m != month or d != day:
            d += 1
            w += 1
            
            if w > 7:
                w = 1
                
            flag = False
            if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                flag = True

            if flag and m == 2:
                if d > 29:
                    m += 1
                    d = 1
            else:
                if d > months[m]:
                    m += 1
                    d = 1
                    
            if m > 12:
                m = 1
                y += 1
        return week[w]