# Let's call an array A a mountain if the following properties hold:
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that 
# A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, 
# return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example 1:
# Input: [0,1,0]
# Output: 1

# Example 2:
# Input: [0,2,1,0]
# Output: 1

# Note:
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above.

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        # M1. 线性扫描 O(n)
        for i in range(1, len(A)-1):
            if A[i-1] < A[i] and A[i] > A[i+1]:
                return i
                
        # 查找第一个下降点
        for i in range(len(A)):
            if A[i] > A[i+1]:
                return i

        # M2. 折半查找 O(lgn)
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
        
