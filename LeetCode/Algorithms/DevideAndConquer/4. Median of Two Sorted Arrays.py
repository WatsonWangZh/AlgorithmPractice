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

        # M1. 模拟 合并sort O((m+n)lg(m+n))
        array = nums1 + nums2
        array.sort()
        
        l = len(array)
        if l % 2 == 0:
            return (array[l//2] + array[l//2 - 1]) / 2.
        else:
            return array[l//2]

        
        # M2. 归并排序 O(m+n)

        tmp = []
        l = (len(nums1) + len(nums2)) // 2 
        flag = (len(nums1) + len(nums2)) % 2

        i, j, cnt = 0, 0, 0
        while i < len(nums1) and j < len(nums2) and cnt < l+1:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
            cnt += 1
            
        while i < len(nums1) and cnt < l+1:
            tmp.append(nums1[i])
            i += 1
            cnt += 1
            
        while j < len(nums2) and cnt < l+1:
            tmp.append(nums2[j])
            j += 1
            cnt += 1
            
        if flag:
            return tmp[-1]
        else:
            return (tmp[-1]+tmp[-2]) / 2.


        # M3. 二分法  O(log(n+m))
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l//2-1)) / 2.

    def kth(self, a, b, k):
        if not a: 
            return b[k]
        if not b: 
            return a[k]

        ia, ib = len(a)//2, len(b)//2
        a_mid, b_mid = a[ia], b[ib]
        if ia + ib < k:
            if a_mid > b_mid: 
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:             
                return self.kth(a[ia + 1:], b, k - ia - 1)
        else:
            if a_mid > b_mid: 
                return self.kth(a[:ia], b, k)
            else:             
                return self.kth(a, b[:ib], k) 