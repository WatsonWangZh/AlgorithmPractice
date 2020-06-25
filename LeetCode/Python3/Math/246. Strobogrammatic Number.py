# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.

# Example 1:
# Input:  "69"
# Output: true

# Example 2:
# Input:  "88"
# Output: true

# Example 3:
# Input:  "962"
# Output: false

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # 双指针 数组遍历 O(n)
        # 这道题定义了一种对称数，就是说一个数字旋转180度和原来一样，也就是倒过来看一样，比如609，倒过来还是609等等，
        # 满足这种条件的数字其实没有几个，只有0,1,8,6,9。
        # 这道题其实可以看做求回文数的一种特殊情况，我们还是用双指针来检测，那么首尾两个数字如果相等的话，那么只有它们是0,1,8中间的一个才行，
        # 如果它们不相等的话，必须一个是6一个是9，或者一个是9一个是6，其他所有情况均返回false。

        # l, r = 0, len(num) - 1

        # while l <= r:
        #     if num[l] == num[r]: 
        #         if num[l] != '1' and num[l] != '0' and num[l] != '8':
        #             return False
        #     else:
        #         if (num[l] != '6' or num[r] != '9') and (num[l] != '9' or num[r] != '6'):
        #             return False
        #     l += 1
        #     r -= 1

        # return True

        # Hash优化 O(n)
        # 由于满足题意的数字不多，所以我们可以用哈希表来做，把所有符合题意的映射都存入哈希表中，
        # 然后双指针扫描，看对应位置的两个数字是否在哈希表里存在映射，若不存在，返回false，遍历完成返回true。

        stored = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}

        for left in range((len(num) + 1) // 2):
            right = len(num) - 1 - left

            if num[left] not in stored or stored[num[left]] != num[right]:
                return False

        return True