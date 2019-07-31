# Remember the story of Little Match Girl? By now, you know exactly 
# what matchsticks the little match girl has, 
# please find out a way you can make one square by using up all those matchsticks. 
# You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Your input will be several matchsticks the girl has, represented with their stick length. 
# Your output will either be true or false, to represent whether you could make one square 
# using all the matchsticks the little match girl has.

# Example 1:
# Input: [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

# Example 2:
# Input: [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
# Note:
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.

# Hints:
# 1. Treat the matchsticks as an array. Can we split the array into 4 equal halves?
# 2. Every matchstick can belong to either of the 4 sides. We don't know which one. Maybe try out all options!
# 3. For every matchstick, we have to try out each of the 4 options i.e. which side it can belong to. 
# We can make use of recursion for this.
# 4. We don't really need to keep track of which matchsticks belong to a particular side during recursion. 
# We just need to keep track of the length of each of the 4 sides.
# 5. When all matchsticks have been used we simply need to see the length of all 4 sides. 
# If they're equal, we have a square on our hands!

class Solution(object):
    # 给定一些整数，代表火柴棍的长度。求这些火柴棍是否可以组成一个正方形。火柴棍不可以拆分，但是可以拼接。
    
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 深度优先搜索 O(4^n)
        # 很明显正方形四条边长一样,因此我们可以求出边长。接下来设置一个SubSum的数组，长度为4，表明当前状态下每条边长的长度。
        # 在深度优先搜索的过程中枚举每根木棍放在第几个边长上。 最后只要前三个边长的长度等于给定的边长，那么剩下的第四个边长一定也和一样。（当然木棍总和如果不是4的倍数要先剔除）
        # 一点优化： 深度优先搜索在寻找的过程中， 深度尽可能的浅时间比较短， 那么我们就将长的木棍放在前面，短的放在后面即可。
        # 时间复杂度分析：每次枚举长度为4，共有n层，故复杂度为O(4^n)

        if len(nums) < 4 or sum(nums) % 4 != 0 or max(nums) > sum(nums) / 4:
            return False
        nums.sort(reverse=True)
        length = sum(nums) / 4
        return self.helper(nums, [length, length, length, length], 0)


    def helper(self, nums, sides, index):
        if index == len(nums):
            return True
        for i in range(4):
            if sides[i] >= nums[index]:
                sides[i] -= nums[index]
                if self.helper(nums, sides, index + 1):
                    return True
                sides[i] += nums[index]
        return False
