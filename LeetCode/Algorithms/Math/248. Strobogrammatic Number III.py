# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

# Example:
# Input: low = "50", high = "100"
# Output: 3 
# Explanation: 69, 88, and 96 are three strobogrammatic numbers.

# Note:
# Because the range might be a large number, the low and high numbers are represented as string.

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        # 参照247题递归求解思路，找出所有符合长度要求的结果，
        # 再根据上下限去除不符合大小要求的结果，并计数。

        res = []
        for i in range(len(low), len(high) + 1):
            res += self.helper(i, i)
        
        count = 0
        for num in res:
            if (len(num) == len(low) and num < low) or (len(num) == len(high) and num > high):
                continue
            count += 1

        return count
            
            
    def helper(self, curr, target):
        if curr == 0:
            return ['']
        if curr == 1:
            return ['0', '1', '8']
            
        subRes = self.helper(curr - 2, target)
        
        res = []
        for item in subRes:
            if curr != target:
                res.append('0' + item + '0')
            res.append('1' + item + '1')
            res.append('6' + item + '9')
            res.append('9' + item + '6')
            res.append('8' + item + '8')
            
        return res
