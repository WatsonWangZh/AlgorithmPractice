# Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

# Example 1:
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666. 
# The maximum number is 9969.

# Example 2:
# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.

# Example 3:
# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
 
# Constraints:
# 1 <= num <= 10^4
# num's digits are 6 or 9.

# Hints:
# Convert the number in an array of its digits.
# Brute force on every digit to get the maximum number.

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        # https://blog.csdn.net/CSerwangjun/article/details/104053280
        # M1. 模拟 
        return str(num).replace('6','9', 1)

        # M2. 模拟
        str_num = str(num)
        if '6' in str_num:
            pos = str_num.index('6')
            list_num = list(str_num)
            list_num[pos] = '9'
            str_num = ''.join(list_num)
            return int(str_num)
        else:
            return num

        # M3. 模拟
        s = str(num)
        lst = []
        for i in s:
            lst.append(i)
        for i in range(len(lst)):
            if lst[i] == '6':
                lst[i] = '9'
                break
        s = ''.join(lst)
        return int(s)
