# Given a n x n matrix where each of the rows and columns are sorted 
# in ascending order, find the kth smallest element in the matrix.
# Note that it is the kth smallest element 
# in the sorted order, not the kth distinct element.

# Example:
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
# return 13.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # M1.heap
        # import heapq
        # 记录(val, row, col)信息
        # heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        # heapq.heapify(heap)
        # ret = 0
        # for _ in range(k):
        #     ret, i, j = heapq.heappop(heap)
        #     if j+1 < len(matrix[0]):
        #         heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        # return ret
    
        # M2.折半查找
        from bisect import bisect
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # <= mid 的数字和小于k
            if sum(bisect(row, mid) for row in matrix) < k: 
                lo = mid + 1
            # <= mid 的数字和大于等于k    
            else:
                hi = mid
        return lo

