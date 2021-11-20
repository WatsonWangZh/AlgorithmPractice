# Suppose an array sorted in ascending order 
# is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. 
# If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

class Solution(object):
    def search(self, nums, target):
        
        # Runtime: 56 ms, faster than 17.95% of Python3
        # Memory Usage: 13.2 MB, less than 5.96% 
        if( len(nums) == 0):
            return -1
        low, high = 0, len(nums)-1
        while high >= low:
            mid = (high + low) // 2
            # If the mid element is the target,return index
            if nums[mid] == target:
                return mid
            # If not,need to determine the rotation point of the array before deviding up to search
            # If the array is rotated in the later half
            elif nums[mid] < nums[low] : 
                if nums[mid] <= target <= nums[high]:  # case :[7 8 0 {1} 2 3 4 5]
                    low = mid + 1
                else:
                    high = mid - 1 
            # If the array is rotated in the preivious half
            else:
                if nums[low] <= target <= nums[mid]:   # case :[4 5 6 {7} 0 1 2]
                    high = mid - 1
                else:
                    low = mid + 1 
        return -1
        
        
        # Runtime: 40 ms, faster than 61.22% of Python3 
        # Memory Usage: 13.3 MB, less than 5.96%
        # if not nums:
        #     return -1
        # else:
        #     start = 0
        #     end = len(nums) - 1
        #     while start <= end:
        #         mid = (start+end) // 2
        #         if nums[mid] == target:
        #             return mid
        #         else:
        #             if nums[start] <= nums[mid]:
        #                 if target >= nums[start] and target < nums[mid]:
        #                     end = mid -1
        #                 else:
        #                     start = mid + 1
        #             elif nums[mid] < nums[end]:
        #                 if target > nums[mid] and target <= nums[end]:
        #                     start = mid + 1
        #                 else:
        #                     end = mid -1
        #     return -1

def main():
    s = Solution()
    print(s.search(nums = [4,5,6,7,0,1,2], target = 0))
    print(s.search(nums = [4,5,6,7,0,1,2], target = 3))

if __name__ == "__main__":
    main()