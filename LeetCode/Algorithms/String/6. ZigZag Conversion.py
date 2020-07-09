# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # M1. 模拟
        if numRows == 1 or len(s) < numRows: 
            return s

        res = [''] * numRows
        row, step = 0, 0

        for c in s:
            res[row] += c
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(res)
            
        # M2. 找规律
        # 对于行数是4的情况：
        # 0     6       12
        # 1   5 7    11 ..
        # 2 4   8 10
        # 3     9
        # 从中我们发现，对于行数是 n 的情况：
        # 对于第一行和最后一行，是公差为 2(n−1) 的等差数列，首项是 0 和 n−1；
        # 对于第 i 行(0<i<n−1)，是两个公差为 2(n−1) 的等差数列交替排列，首项分别是 i 和 2n−i−2；
        # 所以我们可以从上到下，依次打印每行的字符。
        # 时间复杂度分析：每个字符遍历一遍，所以时间复杂度是O(n).
        
        if numRows == 1 or len(s) < numRows: 
            return s
        res = ""
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                j = i
                while j < len(s):
                    res += s[j]
                    j += 2*numRows-2
            else:
                j, k = i, 2*numRows-2-i
                while j < len(s) or k < len(s):
                    if j < len(s):
                        res += s[j]
                        j += 2*numRows-2
                    if k < len(s):
                        res += s[k]
                        k += 2*numRows-2
        return res