# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, 
# and the memory is limited such that you cannot load all elements into the memory at once?

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 哈希表 O(n+m)
        # 首先先将nums1存入哈希表中，然后遍历nums2，
        # 对于每个数 x，如果 x 出现在哈希表中，则将 x 输出，且从哈希表中删除一个 x。
        # 时间复杂度分析：
        # 假设两个数组的长度分别是 n,m。将nums1存入哈希表的计算量是 O(n)，遍历nums2的计算量是 O(m)，
        # 所以总时间复杂度是 O(n+m)。

        # 思考题：
        # 如果给定的数组已经排好序，你可以怎样优化你的算法？
        # 答：可以用双指针扫描。这样可以把空间复杂度降为 O(1)，但时间复杂度还是 O(n)；

        # 如果数组nums1的长度小于数组nums2的长度，哪种算法更好？、
        # 答：可以把nums1存入哈希表，然后遍历nums2。这样可以使用更少的内存，但时空复杂度仍是 O(n)；

        # 如果数组nums2存储在硬盘上，然而内存是有限的，你不能将整个数组都读入内存，该怎么做？
        # 答：如果nums1可以存入内存，则可以将nums1存入哈希表，然后分块将nums2读入内存，进行查找；
        # 如果两个数组都不能存入内存，可以先将两个数组分别排序，
        # 比如可以用外排序，然后用类似于双指针扫描的方法，将两个数组分块读入内存，进行查找。

        result = []
        memo = {}
        for num in nums1:
            memo[num] = memo[num]+1 if num in memo else 1
        for num in nums2:
            if num in memo and memo[num] > 0:
                result.append(num)
                memo[num] -= 1

        return result

