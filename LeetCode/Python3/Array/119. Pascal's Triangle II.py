# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 3
# Output: [1,3,3,1]

# Follow up:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # M1. 模拟 双行
        res = [1]
        for i in range(rowIndex):
            first = [0] + res
            second = res + [0]
            # print(first, second)
            res = [first[n] + second[n] for n in range(len(first))]
        return res

        # M2. 模拟 单行自后向前
        res = [0] * (rowIndex+1)
        res[0] = 1 
        for i in range(1, rowIndex+1):
            # print(res)
            for j in range(rowIndex, 0, -1):
                res[j] = res[j] + res[j-1] 
        return res