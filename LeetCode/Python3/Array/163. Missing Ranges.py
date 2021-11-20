# Given a sorted integer array nums, 
# where the range of elements are in the inclusive range [lower, upper], 
# return its missing ranges.

# Example:
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        # 模拟，数组扫描 O(n)
        # 边界条件的处理
        # 从小到大枚举每个数，枚举过程中维护上一个数的值 pre_num。然后分情况讨论：
        # 当前数等于上一个数，则将 pre_num 置成当前数；
        # 当前数大于上一个数：
        # (1) 只缺失一个数，则直接输出该数；
        # (2) 缺失多个数，则输出区间；
        # 时间复杂度分析：整个数据仅扫描一遍，所以时间复杂度是 O(n)。

        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + '->' + str(upper)]
            
        result = []
        if nums[0] > lower:
            if nums[0] - lower > 1:
                result.append(str(lower) + '->' + str(nums[0] - 1))
            else:
                result.append(str(lower))
             
        pre_num = nums[0]
        for num in nums[1:]:
            if num - pre_num == 2:
                result.append(str(pre_num + 1))
            elif num - pre_num > 2:
                result.append(str(pre_num + 1) + '->' + str(num - 1))
            
            pre_num = num
            
        if upper - pre_num == 1:
            result.append(str(upper))
        elif upper - pre_num > 1:
            result.append(str(pre_num + 1) + '->' + str(upper))
            
        return result
        