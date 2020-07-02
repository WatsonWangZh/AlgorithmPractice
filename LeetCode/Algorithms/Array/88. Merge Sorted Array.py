# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) 
# to hold additional elements from nums2.

# Example:
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 线性合并 时间复杂度 O(m+n), 空间复杂度O(1)
        # 设置cur指针指向合并后的nums1数组(大小为m+n)的最后一个元素，
        # p指向合并前的nums1数组(大小为m)的最后一个元素，
        # q指向nums2数组(大小为n)的最后一个元素。
        # 比较p指向的值和q指向的值，将大的值挪进nums1[cur]。
        # cur指针往前挪，p或者q指针也相应往前挪。
        # 循环以上步骤直到p=0或q=0
        # 若q>=0,将nums2数组剩余的元素挪进nums1。
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        