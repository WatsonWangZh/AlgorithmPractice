# Convert a non-negative integer to its english words representation. 
# Given input is guaranteed to be less than 2^31 - 1.

# Example 1:
# Input: 123
# Output: "One Hundred Twenty Three"

# Example 2:
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"

# Example 3:
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

# Example 4:
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 模拟 O(logn)
        # 为了便于处理，我们将所有单词和数字的映射关系存入哈希表。
        # 然后将原问题分解，我们发现如果可以表示0~999，然后配合 thousand、million、billion即可表示出 10^12以内的所有数。
        # 即: xxx billion xxx million xxx thousand xxx，其中xxx是0~999的表示方式。
        # 然后考虑如何表示1000以内的数，分情况讨论：
        # 如果大于等于100，则需要先写出 x hundred，x是1~9的英文表示；
        # 如果末两位大于20，则需要写出 xx-ty y，xx-ty是20~90的英文表示，y是1~9的英文表示；
        # 如果末两位不超过20，则直接输出相应的英文单词；
        # 时间复杂度分析：计算量与 n 的十进制表示的位数成正比，所以时间复杂度是 O(logn)。

        if num == 0 :
            return "Zero"
        
        LESS_THAN_TWENTY = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]
        
        def helper(n) :
            if n == 0 :
                return ""
            if n < 20 :
                return LESS_THAN_TWENTY[n] + " "
            elif n < 100 :
                return TENS[n//10] + " " + helper(n%10)
            else :
                return LESS_THAN_TWENTY[n//100] + " Hundred " + helper(n%100)

        res, i = "", 0
        
        while num > 0 :
            if num % 1000 != 0 :
                res = helper(num%1000) + THOUSANDS[i] + " " + res
            i += 1
            num //= 1000
        return res.strip()
        