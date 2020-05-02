# Given a sorted array, two integers k and x, find the k closest elements to x in the array. 
# The result should also be sorted in ascending order. 
# If there is a tie, the smaller elements are always preferred.

# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]

# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]

# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 10^4
# Absolute value of elements in the array and x will not exceed 10^4

# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list of integers). 
# Please reload the code definition to get the latest changes.

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # M1. 差值排序 O(nlogn)
        arr = sorted(arr, key = lambda y: abs(x-y))
        return sorted(arr[:k])
        
        # M2. 双指针 O(n)
        # left pointer and right pointer
        i, j = 0, len(arr)-1
        while j-i+1 != k:
            # will stop once we have k elements
            # else keep shifting pointers towards minimum difference
            left_diff = abs(arr[i] - x)
            right_diff = abs(arr[j] - x)
            if left_diff > right_diff:
                i += 1
            else:
                j -= 1
        return arr[i:j+1]
        
        # M3.二分查找 O(logn+k)
        # 使用二分，找到第一个大于等于 x 的位置（若不存在就是最后一个位置）r，然后令 l–。
        # 这里的 l 和 r 代表的是开区间 (l, r) 内的数字保证是最接近 x的。
        # 然后开始枚举，判断 arr[l] 和 arr[r] 谁更接近 x，谁更接近就向左或者向右移动，直到找到 k 个数字为止。
        # 时间复杂度
        # 二分的时间复杂度为 O(logn)，寻找答案的时间复杂度为 O(k)，故总时间复杂度为 O(logn+k)。

        n = len(arr)
        l, r = 0, n-1
        res = []

        while l < r:
            mid = (l + r) >> 1
            if x <= arr[mid]:
                r = mid
            else:
                l = mid + 1
        l -= 1
        
        while r-l-1 < k and (l >= 0 or r < n):
            if l >= 0 and r < n:
                if x - arr[l] <= arr[r] - x:
                    l -= 1
                else:
                    r += 1
            elif l >= 0:
                l -= 1
            else:
                r += 1
                
        for i in range(l+1, r):
            res.append(arr[i])

        return res