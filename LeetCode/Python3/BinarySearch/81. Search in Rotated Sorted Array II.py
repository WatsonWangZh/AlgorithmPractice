# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

# Follow up:
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # M1. One Line Solution
        # return True if target in nums else False

        # M2. 两遍二分 
        # 采用154题二分方法找出最小值，确定target所在分段，之后在分段内再次二分查找
        if not nums:
            return False

        l, t = 0, len(nums) - 1
        while t and nums[t] == nums[0]:
            t -= 1
        r = t

        while l < r:
            mid = l + r >> 1
            if nums[mid] <= nums[t]:
                r = mid
            else:
                l = mid + 1
        
        if target <= nums[t]:
            r = t
        else:
            l = 0
            r -= 1
        
        while l < r:
            mid = l + r >> 1
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid

        return nums[l] == target

        # M3. 一遍二分
        # 我们知道，整个旋转后的数组由两个非严格单调递增的子数组组成，假设[left,right]是当前搜索空间。
        # 如果nums[mid]>nums[right]，说明mid在第一个非严格单调递增子数组中，那么[left,mid]这个区间肯定是非严格单调递增的。
        #   那么如果target在[nums[left],nums[mid])这个区间内，那么搜索范围就会变成[left,mid]。否则搜索范围就会变成[left+1,mid]。
        # 如果nums[mid]<nums[right]，说明mid在第二个非严格单调递增子数组中，那么[mid,right]这个区间肯定是非严格单调递增的。
        #   那么如果target在(nums[mid],nums[right])这个区间内，那么搜索范围就会变成[mid,right]。否则搜索范围就会变成[left+1,mid]。
        # 最后一种情况则是最复杂的。
        # 如果nums[mid]=nums[right]，那么mid既有可能在第一个区间内(从left到mid的数都相等)，也有可能在第二个区间内（从mid到right的值都相等，且等于left）。
        # 假设原数组是[1,2,3,3,3,3,3]，那么旋转之后有可能是[3,3,3,3,3,1,2]，或[3,1,2,3,3,3,3]。这个时候，其实我们只需要将right=right-1就可以了，
        # 因为nums[right]=nums[mid],nums[mid]!=target，那么nums[right]!=target,且mid<right,依然可以保证答案仍在区间所以我们可以将搜索范围缩小。

        if not nums:
            return False

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + r >> 1
            # nums[mid]属于第一部分
            if nums[mid] > nums[r]:
                if target <= nums[mid] and target >= nums[l]:
                    #! 不等价 nums[l] <= target <= nums[mid]
                    r = mid 
                else:
                    l = mid + 1
            # nums[mid]属于第二部分        
            elif nums[mid] < nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:
                r -= 1

        return nums[l] == target
 
        # M3. 另外一种一遍二分写法
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
        return False