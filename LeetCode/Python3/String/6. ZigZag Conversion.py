# The string "PAYPALISHIRING" is written in a zigzag pattern 
# on a given number of rows like this: 
# (you may want to display this pattern 
# in a fixed font for better legibility)

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

class Solution(object):
    def convert(self,s,numRows):

        # M1. 模拟 O(n)
        # if numRows < 2:
        #     return s
        # rows = [''] * numRows
        # idx = 0
        # for ch in s :
        #     rows[idx] += ch
        #     if idx == 0:
        #         direction = 1
        #     elif idx == numRows-1:
        #         direction = -1
        #     idx += direction
        # return ''.join(rows)

        # M2. 找规律 O(n)
        # 这种按某种形状打印字符的题目，一般通过手画小图找规律来做。
        # 我们先画行数是4的情况：
        # 0     6       12
        # 1   5 7    11 ..
        # 2 4   8 10
        # 3     9
        # 从中我们发现，对于行数是 n 的情况：
            # 对于第一行和最后一行，是公差为 2(n−1) 的等差数列，首项是 0 和 n−1；
            # 对于第 i 行(0<i<n−1)，是两个公差为 2(n−1) 的等差数列交替排列，首项分别是 i 和 2n−i−2；
        # 所以我们可以从上到下，依次打印每行的字符。
        # 时间复杂度分析：每个字符遍历一遍，所以时间复杂度是O(n).

        if numRows < 2:
                return s
        res = ""
        for i in range(numRows):
                line = []
                if i == 0:
                        line = [s[j] for j in range(0, len(s), 2*(numRows-1))]
                elif i == numRows - 1:
                        line = [s[j] for j in range(numRows-1, len(s), 2*(numRows-1))]    
                else:
                        line=[s[j] for j in range(i, len(s), 2*(numRows-1))]
                        temp=[s[j] for j in range(2*numRows-i-2, len(s), 2*(numRows-1))]
                        line = self.merge(line, temp)
                res += "".join(line)
        return res

    ##实现两个不等长数组的交叉合并，[1,3,5,7] + [2,4,6] = [1,2,3,4,5,6,7]
    def merge(self, nums1, nums2):
        res = []
        for i in range(max(len(nums1), len(nums2))):
                if nums1:
                        res.append(nums1.popleft()) 
                if nums2:
                        res.append(nums2.popleft())
        return res

        # M3. 另外一种规律 O(n)
        # if numRows < 2:
        #     return s
        # rows = [''] * numRows
        # for i,char in enumerate(s):
        #     idx = i % (2*(numRows-1))
        #     if idx < numRows:
        #         rows[idx] += char
        #     else:
        #         rows[numRows-2-idx] += char
        # return ''.join(rows)
