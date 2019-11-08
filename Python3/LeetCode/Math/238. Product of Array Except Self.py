# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal to the product of all the elements of nums 
# except nums[i].

# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).
# Follow up:
# Could you solve it with constant space complexity? 
# (The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 题目特殊限制不让用除法
        # 采用前缀后缀积 即分别计算待操作位置左右两侧元素之积 O(n) O(1)
        # 利用output数组当做临时存储空间，令output[i]为从nums[0]*nums[1]*…*num[i−1]。
        # 然后从数组末尾，用变量end记录末尾若干数字的乘积，每次更新output[i]即可得到答案。
        # 时间复杂度
        # 只扫描数组两次，故时间复杂度为O(n)。
        # 空间复杂度
        # 除output数组之外只使用了若干变量，故空间复杂度为O(1)。

        if not nums:
            return None
        l = len(nums)
        output = [1 for i in range(l)]
        output[0] = 1
        for i in range(1,l):
            output[i] = output[i-1] * nums[i-1]

        end = 1
        for i in range(l-2, -1, -1):
            end = end * nums[i+1]
            output[i] = output[i] * end

        return output
