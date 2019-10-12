# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, 
# return a sorted array of only the integers that appeared in all three arrays.

# Example 1:
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.

# Constraints:
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000

# Hints:
# Count the frequency of all elements in the three arrays.
# The elements that appeared in all the arrays would have a frequency of 3.
from collections import Counter
class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        # M1. set求交集
        # return sorted(set(arr1) & set(arr2) & set(arr3))

        # M2. Counter计数，值是否为3
        # return [k for k, v in Counter(arr1 + arr2 + arr3).items() if v == 3]

        # M3. 三指针移动
        # 由于三个数组已经是排好序的，所以我们用三个指针分别从头指向这三个数组，然后依次遍历。
        # 如果当前这三个指针指向的数字相同，则加入到答案数组中，三个指针依次后移。
        # 否则，我们找到三个指针中最小的元素，移动所有和这个最小元素相同的指针。
        # 当其中一个指针到达末尾后，退出循环。

        l1, l2, l3 = len(arr1), len(arr2), len(arr3)
        res = []
        i = j = k = 0
        while i < l1 and j < l2 and k < l3:
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                min_ele = min(arr1[i], arr2[j], arr3[k])
                if arr1[i] == min_ele:
                    i += 1
                if arr2[j] == min_ele:
                    j += 1
                if arr3[k] == min_ele:
                    k += 1
        return res