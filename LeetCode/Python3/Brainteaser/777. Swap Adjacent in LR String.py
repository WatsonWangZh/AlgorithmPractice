# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", 
# a move consists of either replacing one occurrence of "XL" with "LX", 
# or replacing one occurrence of "RX" with "XR". 
# Given the starting string start and the ending string end, 
# return True if and only if there exists a sequence of moves to transform one string to the other.

# Example:
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
 
# Constraints:
# 1 <= len(start) == len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.

# Hints:
# Think of the L and R's as people on a horizontal line, where X is a space. 
# The people can't cross each other, and also you can't go from XRX to RXX.

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        n = len(start)
        sL, sR, eL, eR = 0, 0, 0, 0
        
        for i in range(n):
            if start[i] == 'L':
                sL += 1
            if start[i] == 'R':
                sR += 1
            if end[i] == 'L':
                eL += 1
            if end[i] == 'R':
                eR += 1
            if sL > eL or sR < eR:
                return False
        return sL == eL and sR == eR and sL + sR < n and start.replace('X','') == end.replace('X', '')
