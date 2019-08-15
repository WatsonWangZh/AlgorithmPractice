# Given a circular array C of integers represented by A, 
# find the maximum possible sum of a non-empty subarray of C.
# Here, a circular array means the end of the array connects to the beginning of the array.  
# (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
# Also, a subarray may only include each element of the fixed buffer A at most once.  
# (Formally, for a subarray C[i], C[i+1], ..., C[j], 
# there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

# Example 1:
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3

# Example 2:
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

# Example 3:
# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

# Example 4:
# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

# Example 5:
# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
 
# Note:
# -30000 <= A[i] <= 30000
# 1 <= A.length <= 30000

class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 前缀和，单调队列 O(n)
        # 将原数组扩充一倍后，这道题可以视为长度最多为 n 最长连续子序列。先求前缀和数组 prefix_sum。
        # 对于以 i 结尾的子数组，其最优答案是 prefix_sum[i] − min(prefix_sum[j]), i−n ≤ j < i。
        # 在所有以 i 结尾的子数组中找到最大值即为答案。
        
        # 以上公式可以用单调队列来快速求解。
        # 维护一个单调递增的队列，队头元素为最小值，每次循环时首先将不满足长度的队头出队，然后更新当前的答案。
        # 入队时，检查队尾元素与当前 prefix_sum[i] 值的大小，如果 prefix_sum[i] 小于等于队尾元素，则队尾元素出队。
        # 最后 sum[i] 进队。

        # 时间复杂度
        # 每个元素最多进队一次，出队一次，故总时间复杂度为 O(n)。

        n = len(A)
        prefix_sum = [0] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            if i <= n:
                prefix_sum[i] = prefix_sum[i-1] + A[i-1]
            else:
                prefix_sum[i] = prefix_sum[i-1] + A[i-n-1]

        import collections
        queue = collections.deque()
        queue.append(0)
        result = A[0]

        for i in range(1, 2*n+1):
            while queue and i - queue[0] > n:
                queue.popleft()

            result = max(result, prefix_sum[i]-prefix_sum[queue[0]])

            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()

            queue.append(i)

        return result
