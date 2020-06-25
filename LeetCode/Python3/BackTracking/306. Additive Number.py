# Additive number is a string whose digits can form additive sequence.
# A valid additive sequence should contain at least three numbers. 
# Except for the first two numbers, 
# each subsequent number in the sequence must be the sum of the preceding two.
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
# Note: Numbers in the additive sequence cannot have leading zeros, 
# so sequence 1, 2, 03 or 1, 02, 3 is invalid.

# Example 1:
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
#              1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

# Example 2:
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199. 
#              1 + 99 = 100, 99 + 100 = 199
 
# Constraints:
# num consists only of digits '0'-'9'.
# 1 <= num.length <= 35

# Follow up:
# How would you handle overflow for very large input integers?

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # 递归模拟 长度限制
        if len(num) < 3:
            return False

        for i in range(len(num)/2):
            first = int(num[0:i+1])
            if i >= 1 and num[0] == '0': 
                continue
            if self.lookForSecondNum(first, num[i+1:]):
                return True

        return False

    def lookForSecondNum(self, first, num):
        for i in range(len(num)/2):
            second = int(num[0:i+1])
            if i >= 1 and num[0] == '0': 
                return False
            if self.lookForThirdNum(first, second, num[i+1:]):
                return True

        return False

    def lookForThirdNum(self, previous1, previous2, num):
        if len(num) == 0:
            return True
        
        target = previous1 + previous2
        target_s = str(target)
        if num[:len(target_s)] == target_s:
            return self.lookForThirdNum(previous2, target, num[len(target_s):])
            
        return False