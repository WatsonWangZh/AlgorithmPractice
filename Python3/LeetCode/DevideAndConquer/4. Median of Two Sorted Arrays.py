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

        # M1. 合并数组，直接查找
        # array = nums1 + nums2
        # array.sort()
        # length = len(array)
        # if length % 2 == 0:
        #     median = (array[length/2] + array[length/2 - 1]) / 2.0
        # else:
        #     median = float(array[length/2])
        # return median
        
        # M2. (递归) O(log(n+m))
        # 原问题难以直接递归求解，所以我们先考虑这样一个问题：
        #   在两个有序数组中，找出第k大数。
        # 如果该问题可以解决，那么第 (n+m)/2 大数就是我们要求的中位数.

        # 先从简单情况入手，
        #  假设 m,n≥k/2，我们先从 nums1 和 nums2 中各取前 k/2 个元素：
        #   如果 nums1[k/2−1]>nums2[k/2−1]，则说明 nums1 中取的元素过多，nums2 中取的元素过少；
        #       因此 nums2 中的前 k/2 个元素一定都小于等于第 k 大数，
        #       所以我们可以先取出这些数，将问题归约成在剩下的数中找第 k−⌊k/2⌋ 大数.
        #   如果 nums1[k/2−1]≤nums2[k/2−1]，同理可说明 nums1 中的前 k/2 个元素一定都小于等于第 k 大数，
        #       类似可将问题的规模减少一半.

        # 现在考虑边界情况，
        #   如果 m<k/2，则我们从 nums1 中取m个元素，从nums2 中取 k/2 个元素,（由于 k=(n+m)/2，因此 m,n 不可能同时小于 k/2）：
        #       如果 nums1[m−1]>nums2[k/2−1，则 nums2 中的前 k/2 个元素一定都小于等于第 k 大数，
        #           我们可以将问题归约成在剩下的数中找第 k−⌊k/2⌋ 大数.
        #       如果 nums1[m−1]≤nums2[k/2−1]，则 nums1 中的所有元素一定都小于等于第 k 大数，
        #           因此第k大数是 nums2[k−m−1].

        # 时间复杂度分析：
        # k=(m+n)/2, 且每次递归 k 的规模都减少一半，因此时间复杂度是 O(log(m+n))

        # l1, l2 = len(nums1), len(nums2)
        # t = l1 + l2 

        # if t % 2 == 1:
        #     return findKth(nums1, nums2, t//2)
        # else:
        #     l = findKth(nums1, nums2, t//2)
        #     r = findKth(nums1, nums2, t//2 - 1)
        #     return (l + r) / 2.0

        # import bisect

        # def getMedian(a):
        #     l = len(a)
        #     h = l // 2
        #     if l % 2:
        #         return h, a[h]
        #     else:
        #         return h-1, (a[h] + a[h-1]) / 2.0
        
        # def findKth(a, b, k):
        #     la, lb = len(a), len(b)
        #     if la <= 2:
        #         s = [e for e in b]
        #         for n in a:
        #             bisect.insort_left(s, n)
        #         return s[k]
            
        #     if lb <= 2:
        #         s = [e for e in a]
        #         for n in b:
        #             bisect.insort_left(s, n)
        #         return s[k]
            
        #     if k <= 1:
        #         s = s[:2] + b[:2]
        #         s.sort()
        #         return s[k]

        #     delta = k // 2
        #     if la <= delta:
        #         return findKth(a, b[delta:], k-delta)
        #     elif lb <= delta:
        #         return findKth(a[delta:], b, k-delta)
        #     else:
        #         if a[delta] > b[delta]:
        #             return findKth(a, b[delta:], k-delta)
        #         else:
        #             return findKth(a[delta:], b, k-delta)
    

        # M3. 二分 O(log(min(m,n))
        # 该算法的处理细节非常繁琐，建议新手直接跳过。
        # 首先，让我们考虑只有一个有序数组的情况：
        # 如果我们将有序数组切分为等长的左右两部分，则 中位数 = (左半边的最大值 + 右半边的最小值) / 2.
        # 切分情况有两种，例如：
        #   数组长度是偶数，对于 [2 3 5 7], 我们在3和5之间切分：[2 3 / 5 7]，则 中位数 =(3+5)/2=(3+5)/2；
        #   数组长度是奇数，对于 [2 3 4 5 7]，我们在4的位置切分，且让4属于左右两边：[2 3 (4/4) 5 7]，
        #                则 中位数 =(4+4)/2.

        # 现在让我们来考虑两个有序数组的情况，类似于上述考虑方式：
        # 我们在两个数组中分别找到一个分割点（分割点可能在相邻数之间，也可能在数上），
        # 两个分割点左边元素的总个数等于右边元素的总个数，且左边元素的最大值 <= 右边元素的最小值，则该分割点即为所求。

        # 为了同时处理分割点在两数之间和在数上的情况，我们在数组中可能是分割点的位置添加虚拟元素 ‘@’，
        # 这样我们枚举数组 A1′ 的所有元素，即可枚举 A1 所有可能的分割点：
        # A1:[1,2,3,4,5]=>A1′:[@,1,@,2,@,3,@,4,@,5,@]
        # A2:[1,1,1,1]=>A2′:[@,1,@,1,@,1,@,1,@]
        # 我们将数组 A1 的长度记为 N1，则 A1′ 的长度为 2*N1+1; A2 的长度记为 N2，则 A2′ 的长度为 2*N2+1. 
        # 总共有 2N1+2N2+2 个元素.

        # 假设数组 A1′ 的分割点下标是 C1，数组 A2′ 的分割点下标是 C2，则 C1 和 C2 之间具有如下等式关系：
        # C1 + C2 = N1 + N2

        # 证明：
        # 除了 C1 和 C2 以外，共有 2N1 + 2N2 个元素，要平均分配到左右两边，因此左边共有 N1+N2 个元素. 
        # 数组下标从0开始，下标为 C1 的元素左边有 C1 个元素，下标为 C2 的元素左边有 C2 个元素，由此可得上述等式.

        # 为了方便表述，
        # 在 A1′ 中，C1 左边（包括C1）的最大值记为 L1，C1 右边（包括C1）的最小值记为 R1；
        # 在 A2′ 中，C2 左边（包括C2）的最大值记为 L2，C2 右边（包括C2）的最小值记为 R2；
        # 则如果我们选取的分割点满足
        # L1 <= R1 && L1 <= R2 && L2 <= R1 && L2 <= R2
        # 则分割点即为所求. 由于 A1,A2 都是有序的，因此 L1 <= R1 && L2 <= R2 一定满足；
        # 不满足的情况有两种：
        #   如果 L1>R2，表示 A2 中在分割点左侧的元素太少，此时我们需要将 C2 右移；
        #   如果 L2>R1，表示 A2 中在分割点左侧的元素太多，此时我们需要将 C2 左移；
        #   符合二分结构.
        # 另外，我们在实际操作中，不需要真的在原数组中插入 ‘@’，只需找出 L1,R1,L2,R2 和 C1,C2 的关系即可.
        # 我们可以列表找规律：
        # C1	L1	        R1
        # 0	    INT_MIN	    A1[0]
        # 1	    A1[0]	    A1[0]
        # 2	    A1[0]	    A1[1]
        # 3	    A1[1]	    A1[1]
        # 4	    A1[1]	    A1[2]
        # 由此我们可以发现:
        # L1 = A1[(C1−1)/2]
        # R1 = A1[C1/2]
        # 类似可得：
        # L2 = A2[(C2−1)/2]
        # R2 = A2[C2/2]
        # 最后，还有两点需要注意：
        # 我们只能二分长度较小的数组，因为长度较长的数组中的某些分割点可能不合法，会出现 C1 > N1+N2 的情况；
        # 我们在数组边界设置两个哨兵，来处理 C1=0 或 C1 = 2N1 的情况：A1[−1]=INTMIN,A1[2N]=INTMAX. 
        # 这样做并不会影响结果，但可以简化代码.
        # 时间复杂度：二分长度较短的数组，且每次二分的复杂度是 O(1)，
        # 所以总复杂度是 O(log(min(n,m))).
        
        # Assume first parameter is the shorted array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        l1, l2 = len(nums1), len(nums2)
        low, high = 0, l1
        while low <= high:
            partition_l1 = (low + high) // 2
            partition_l2 = (l1 + l2 + 1) // 2 - partition_l1
            maxLeft_l1 = float('-inf') if partition_l1 == 0 else nums1[partition_l1 - 1]
            minRight_l1 = float('inf') if partition_l1 == l1 else nums1[partition_l1]
            maxLeft_l2 = float('-inf') if partition_l2 == 0 else nums2[partition_l2 - 1]
            minRight_l2 = float('inf') if partition_l2 == l2 else nums2[partition_l2]

            # Found condition
            if maxLeft_l1 <= minRight_l2 and maxLeft_l2 <= minRight_l1:
                if (l1 + l2) % 2 == 0:
                    return (max(maxLeft_l1, maxLeft_l2) + min(minRight_l1, minRight_l2)) / 2.0 
                else:
                    return max(maxLeft_l1, maxLeft_l2)
            elif maxLeft_l1 > minRight_l2:
                high = partition_l1 - 1 
            else:
                low = partition_l1 + 1

        # M4. 二分法的另一种实现方式
        # A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        # if m > n: 
        #     A, B, m, n = B, A, n, m
        # if n == 0: 
        #     raise ValueError
        
        # imin, imax, half_len = 0, m, int((m+n+1)/2)
        
        # while imin <= imax:
        #     i = int((imin + imax) / 2)
        #     j = half_len - i
            
        #     if i < m and B[j-1] > A[i]:
        #         # i is too small, must increase it
        #         imin = i+1
        #     elif i > 0  and A[i-1] > B[j]:
        #         # i is too big, must decrease it
        #         imax = i-1
        #     else:
        #         # i is perfect
        #         if i == 0: 
        #             max_of_left = B[j-1]
        #         elif j == 0: 
        #             max_of_left = A[i-1]
        #         else: 
        #             max_of_left = max(B[j-1], A[i-1])
                
        #         if (m+n)%2 == 1:
        #             return max_of_left
                
        #         if i == m: 
        #             min_of_right = B[j]
        #         elif j == n: 
        #             min_of_right = A[i]
        #         else: 
        #             min_of_right = min(B[j], A[i])

        #         return (max_of_left+min_of_right) / 2.0
