# Given an array A of integers, return true if and only if we can 
# partition the array into three non-empty parts with equal sums.
# Formally, we can partition the array if we can find indexes i+1 < j 
# with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

# Example 1:
# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

# Example 2:
# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false

# Example 3:
# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 
# Note:
# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000

# Hints:
# If we have three parts with the same sum, what is the sum of each? 
# If you can find the first part, can you find the second part?

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # 线性扫描 O(n)
        # 首先求出整个数组的和sum，如果sum不能被3整除，则直接返回false；
        # 然后令 s = sum / 3；再从头开始扫描数组，如果当前位置i的前缀和等于s，
        # 则从数组末尾开始往前求后缀和，如果发现位置j的后缀和等于s，且i+1<j,则返回true；否则直接返回false。
        # 时间复杂度分析：
        # 扫描两次数组，时间复杂度为O(n)
        # 空间复杂度：
        # 仅定义了若干个遍历，故空间复杂度为O(1)。

        A_sum = 0
        for i in range(len(A)):
            A_sum += A[i]
        if A_sum % 3:
            return False 

        s = A_sum / 3

        temp_sum = 0 
        for i in range(len(A)):
            temp_sum += A[i]
            if temp_sum == s:
                temp_sum = 0
                
                for j in range(len(A)-1, i+1, -1):
                    temp_sum += A[j]
                    if temp_sum == s:
                        return True

                return False
        return False