# Given an unsorted array of integers, 
# find the length of the longest consecutive elements sequence.
# Your algorithm should run in O(n) complexity.

# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.

# 构建hashset，删除当前元素，判断当前元素的-1，+1是否在hashset中，向两端扩展，直到不能扩展
# 这里再说下，为啥当检测某数字在集合中存在当时候，都要移除数字。
# 这是为了避免大量的重复计算，就拿题目中的例子来说吧，我们在遍历到4的时候，会向下遍历3，2，1，
# 如果都不移除数字的话，遍历到1的时候，还会遍历2，3，4。同样，遍历到3的时候，向上遍历4，向下遍历2，1，
# 等等等。如果数组中有大量的连续数字的话，那么就有大量的重复计算，十分的不高效，所以我们要从HashSet中移除数字。

class Solution:
    def longestConsecutive(self, nums):
        ans = 0
        nums = set(nums)
        mpl = mpr = {}
        for i in nums:
            l = mpl[i-1] if i-1 in mpl else i
            r = mpr[i+1] if i+1 in mpr else i 
            mpr[l] = r 
            mpl[r] = l 
            ans = max(r-l+1, ans)
        return ans  
