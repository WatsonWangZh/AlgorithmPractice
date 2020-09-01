# Given an array of 4 digits, 
# return the largest 24 hour time that can be made.
# The smallest 24 hour time is 00:00, and the largest is 23:59.  
# Starting from 00:00, a time is larger if more time has elapsed since midnight.
# Return the answer as a string of length 5.  
# If no valid time can be made, return an empty string.

# Example 1:
# Input: [1,2,3,4]
# Output: "23:41"

# Example 2:
# Input: [5,5,5,5]
# Output: ""
 
# Note:
# A.length == 4
# 0 <= A[i] <= 9

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        # 穷举
        for i in range(23,-1, -1):
            for j in range(59, -1, -1):
                tmp = [int(m) for m in str(i)] + [int(n) for n in str(j)]
                while len(tmp) < 4:
                    tmp.append(0)
                if sorted(tmp) == sorted(A):
                    return str(i).zfill(2) + ':' + str(j).zfill(2)
        return ''

        # 穷举
        res = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > res:
                res = time

        return "{:02}:{:02}".format(res//60, res%60) if res >= 0 else ""