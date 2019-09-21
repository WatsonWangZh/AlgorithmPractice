# Given a number N, return true if and only if it is a confusing number, 
# which satisfies the following condition:
# We can rotate digits by 180 degrees to form new digits. 
# When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. 
# When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. 
# A confusing number is a number that when rotated 180 degrees becomes a different number 
# with each digit valid.

# Example 1:
# Input: 6
# Output: true
# Explanation: 
# We get 9 after rotating 6, 9 is a valid number and 9!=6.

# Example 2:
# Input: 89
# Output: true
# Explanation: 
# We get 68 after rotating 89, 86 is a valid number and 86!=89.

# Example 3:
# Input: 11
# Output: false
# Explanation: 
# We get 11 after rotating 11, 11 is a valid number but the value remains the same, 
# thus 11 is not a confusing number.

# Example 4:
# Input: 25
# Output: false
# Explanation: 
# We get an invalid number after rotating 25.

# Note:
# 0 <= N <= 10^9
# After the rotation we can ignore leading zeros, 
# for example if after rotation we have 0008 then this number is considered as just 8.

# Hints:
# Reverse each digit with their corresponding new digit if an invalid digit is found the return -1. 
# After reversing the digits just compare the reversed number with the original number.

class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # 字典保存可翻转字符对应翻转后的结果，然后遍历字符串，若其中出现无效数字，返回false，
        # 否则对每一位数字进行翻转，看翻转后的数字和原来的数字是否相等。
        
        valids = {"0":"0", "1":"1", "6":"9", "9":"6", "8":"8"}
        s = str(N)
        newS = ""

        for i in range(len(s)):
            if s[i] not in valids:
                return False
            newS += valids[s[i]]
            return False
        return True