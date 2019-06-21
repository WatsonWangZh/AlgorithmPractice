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
        if numRows < 2:
            return s
        m = ['']*numRows
        i = 0
        for ch in s :
            m[i] += ch
            if i == 0:
                direction = 1
            elif i == numRows-1:
                direction = -1
            i += direction
        return ''.join(m)

def main():
    s = Solution()
    print(s.convert(s = "PAYPALISHIRING", numRows = 3))
    print(s.convert(s = "PAYPALISHIRING", numRows = 4))

if __name__ == "__main__":
    main()