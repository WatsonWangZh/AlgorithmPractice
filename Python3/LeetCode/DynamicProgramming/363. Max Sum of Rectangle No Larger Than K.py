# Given a non-empty 2D matrix matrix and an integer k, 
# find the max sum of a rectangle in the matrix such that its sum is no larger than k.

# Example:
# Input: matrix = [
#                   [1,0,1],
#                   [0,-2,3]], k = 2
# Output: 2 
# Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
#              and 2 is the max number no larger than k (k = 2).
# Note:
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # https://blog.csdn.net/fuxuemingzhu/article/details/83014580
        # https://www.acwing.com/solution/LeetCode/content/2982/

        # M1. 暴力求解(TLE)
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        sums = [[0] * N for _ in range(M)]
        res = float("-inf")
        for m in range(M):
            for n in range(N):
                t = matrix[m][n]
                if m > 0:
                    t += sums[m - 1][n]
                if n > 0:
                    t += sums[m][n - 1]
                if m > 0 and n > 0:
                    t -= sums[m - 1][n - 1]
                sums[m][n] = t
                for r in range(m + 1):
                    for c in range(n + 1):
                        d = sums[m][n]
                        if r > 0:
                            d -= sums[r - 1][n]
                        if c > 0:
                            d -= sums[m][c - 1]
                        if r > 0 and c > 0:
                            d += sums[r - 1][c - 1]
                        if d <= k:
                            res = max(res, d)
        return res


        # M2. Kadane’s algorithm (TLE)
        if not matrix or not matrix[0]: return 0
        L, R = 0, 0
        curSum, maxSum = float('-inf'), float('-inf')
        maxLeft, maxRight, maxUp, maxDown = 0, 0, 0, 0
        M, N = len(matrix), len(matrix[0])
        for L in range(N):
            curArr = [0] * M
            for R in range(L, N):
                for m in range(M):
                    curArr[m] += matrix[m][R]
                curSum = self.getSumArray(curArr, M, k)
                if curSum > maxSum:
                    maxSum = curSum
        return maxSum
            
    def getSumArray(self, arr, M, k):
        sums = [0] * (M + 1)
        for i in range(M):
            sums[i + 1] = arr[i] + sums[i]
        res = float('-inf')
        for i in range(M):
            for j in range(i + 1, M + 1):
                curSum = sums[j] - sums[i]
                if curSum <= k and curSum > res:
                    res = curSum
        return res

        # M3. Kadane’s algorithm + 二分查找 (Accepted)
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        M = max(m, n)
        N = min(m, n)
        ans = None
        for x in range(N):
            sums = [0] * M
            for y in range(x, N):
                slist, num = [], 0
                for z in range(M):
                    sums[z] += matrix[z][y] if m > n else matrix[y][z]
                    num += sums[z]
                    if num <= k:
                        ans = max(ans, num)
                    i = bisect.bisect_left(slist, num - k)
                    if i != len(slist):
                        ans = max(ans, num - slist[i])
                    bisect.insort(slist, num)
        return ans or 0

        # M4. Kadane’s algorithm + 二分查找 (Accepted)
        m, n = len(matrix), len(matrix[0])
        M, N = min(m, n), max(m, n)
        ans = None
        
        def findMaxArea(sums, beg, end):
            if beg + 1 >= end:
                return None
            mid = (beg + end) // 2
            res = max(findMaxArea(sums, beg, mid), findMaxArea(sums, mid, end))
            i = mid
            for l in sums[beg:mid]:
                while i < len(sums) and sums[i] - l <= k:
                    res = max(res, sums[i]-l)
                    i += 1
            sums[beg:end] = sorted(sums[beg:end])
            return res
        
        for i1 in range(M):
            tmp = [0] * N
            for i2 in range(i1, M):
                sums, low, maxArea = [0], 0, None
                for j in range(N):
                    tmp[j] += matrix[i2][j] if m <= n else matrix[j][i2]
                    sums.append(sums[-1] + tmp[j])
                    maxArea = max(maxArea, sums[-1]-low)
                    low = min(low, sums[-1])
                if maxArea <= ans:
                    continue
                if maxArea == k:
                    return k
                if maxArea > k:
                    maxArea = findMaxArea(sums, 0, N+1)
                ans = max(ans, maxArea)
        return ans or 0


        # M5. Top Code
        if len(matrix) == 0:
            return 0
        
        # prefix_sum[r][c] gives the sum of the first c elements on row r
        prefix_sum = [None] * len(matrix)
        for r in xrange(len(matrix)):
            prefix_sum[r] = [0] * (len(matrix[r]) + 1)
            prefix_sum[r][0] = 0
            for c in xrange(1, len(matrix[r]) + 1):
                prefix_sum[r][c] = prefix_sum[r][c-1] + matrix[r][c-1]
                
        # Idea is transform the 2-D case into 1-D. For every possible pairs
        # of columns (c_i, c_j), we can look at the partial row sum as an element
        # in a 1-D array. Then we are looking for the maximum possible sum <= k
        # in the 1-D array of partial row sums.
        
        max_s = float('-inf')
        for c_i in xrange(len(matrix[0])):
            for c_j in xrange(c_i, len(matrix[0])):
                # This is kadane's algorithm for quick optimization, may not be necessary
                s = 0
                max_continguous_sum = float('-inf')
                for r in xrange(len(matrix)):
                    # This would cover all the elements on row r in columns [c_i, c_j], inclusive
                    partial_row_sum = prefix_sum[r][c_j+1] - prefix_sum[r][c_i]
                    if s + partial_row_sum >= partial_row_sum:
                        s += partial_row_sum
                    else:
                        s = partial_row_sum
                    max_continguous_sum = max(max_continguous_sum, s)
                    
                if max_continguous_sum <= k:
                    max_s = max(max_s, max_continguous_sum)
                    continue
                 
                # Kadane would give you the subarray with the maximum contiguous sum. But if
                # that sum is > k, it's possible we could get a better sum <= k by dropping
                # some numbers in the front of the subarray. But we don't know which one to 
                # drop, we'll need to resort more trickery below to find out better candidates
                # of `max_s`
                
                cs = 0
                # Tricky code! Now let's compute the prefix_partial_row_sum where
                # prefix_partial_row_sum[r_i] is the sum of all the partial_row_sums in rows [0..r_i].
                # Given some prefix_partial_row_sum[r_j] if there exists some r_i such that
                # prefix_partial_row_sum[r_j] - prefix_partial_row_sum[r_i] <= k (there may be 
                # several instances of such partial_row_sums[r_i]), then the smallest 
                # prefix_partial_row_sum[r_i] >= prefix_partial_row_sum[r_j] - k would 
                # result in the largest possible value of
                # prefix_partial_row_sum[r_j] - partial_row_sums[r_i] <= k
                # , which is exactly what we are looking for!
                # Important: 0 is a valid prefix sum for the initial empty set of partial row sums.
                # Otherwise we'd never consider the prefix_partial_row_sum that includes only the
                # first row or all of the rows
                prefix_partial_row_sum = [0]
                for nb_rows in xrange(1, len(matrix) + 1):
                    r_j = nb_rows - 1
                    partial_row_sum = prefix_sum[r_j][c_j+1] - prefix_sum[r_j][c_i]
                    cs += partial_row_sum # cs is partial_row_sum_r_j
                    
                    # Which of the previously seen prefix_partial_row_sum[r_i], r_i < r_j, would
                    # satisify prefix_partial_row_sum[r_j] - partial_row_sums[r_i] <= k? 
                    # And we want the smallest possible one.
                    # (Note prefix_partial_row_sum is sorted so the previously seen prefix_partial_row_sum
                    # entries are not in order by row index, it doesn't matter, we only want to know
                    # which of those r_i, r_i < r_j)
                    r_i = bisect.bisect_left(prefix_partial_row_sum, cs - k)
                    if r_i < len(prefix_partial_row_sum):
                        max_s = max(max_s, cs - prefix_partial_row_sum[r_i])
                    # Ensure the list is sorted for bsearch to work.
                    bisect.insort(prefix_partial_row_sum, cs)
        
        return max_s