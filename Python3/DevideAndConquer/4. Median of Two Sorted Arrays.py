# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        if m > n: A, B, m, n = B, A, n, m
        if n == 0: raise ValueError
        
        imin, imax, half_len = 0, m, int((m+n+1)/2)
        
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i+1
            elif i > 0  and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i-1
            else:
                # i is perfect
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(B[j-1], A[i-1])
                
                if (m+n)%2 == 1:
                    return max_of_left
                
                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(B[j], A[i])
                
                return (max_of_left+min_of_right)/2.0