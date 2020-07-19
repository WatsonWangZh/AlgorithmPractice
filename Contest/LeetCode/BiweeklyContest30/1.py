# 1507. Reformat Date
# User Accepted:4062
# User Tried:4202
# Total Accepted:4144
# Total Submissions:7015
# Difficulty:Easy
# Given a date string in the form Day Month Year, where:
# Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
# Year is in the range [1900, 2100].
# Convert the date string to the format YYYY-MM-DD, where:
# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day.
 
# Example 1:
# Input: date = "20th Oct 2052"
# Output: "2052-10-20"

# Example 2:
# Input: date = "6th Jun 1933"
# Output: "1933-06-06"

# Example 3:
# Input: date = "26th May 1960"
# Output: "1960-05-26"
 
# Constraints:
# The given dates are guaranteed to be valid, so no error handling is necessary.

class Solution:
    def reformatDate(self, date: str) -> str:
        lst = date.split(' ')

        res = ''
        day = ''
        for c in lst[0]:
            if '0' <= c <= '9':
                day += c

        dic = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04',
               "May": '05', "Jun": '06', "Jul": '07', "Aug": '08',
               "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}

        res += str(lst[2]) + '-' + dic[lst[1]] + '-'
        res += day if len(day) > 1 else '0' + day
        return res

        # awice https://leetcode.com/awice/
        res = []
        d, m, y = date.split()
        res.append(y)

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        i = months.index(m)
        i += 1
        i = str(i).zfill(2)
        res.append(i)

        j = "".join(c for c in d if c.isdigit())
        j = j.zfill(2)
        res.append(j)

        return "-".join(res)