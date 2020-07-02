# Given an array nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position. 
# Return the max sliding window.

# Example:
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 

# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

# Follow up:
# Could you solve it in linear time?

# Hints:
# How about using a data structure such as deque (double-ended queue)?
# The queue size need not be the same as the window’s size.
# Remove redundant elements and the queue should store only elements that need to be considered.

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 单调队列 O(n)
        # 使用单调队列求解滑动窗口中的最大值。其中，单调队列是一个普通的双端队列，即队头和队尾都可以添加和删除元素和弹出元素。
        # 我们假设该双端队列的队头是整个队列的最大元素所在的下标，至队尾下标代表的元素值依次降低。
        # 初始时，单调队列为空，随着对数组的遍历过程中，每次插入元素前，需要考察两个事情：
        # (1)合法性检查：队头下标如果距离i超过了k，则应该出队。
        # (2) 单调性维护：如果nums[i] 大于或等于队尾元素下标对应的值，则当前队尾再也不可能充当某个滑动窗口的最大值了，
        #               故需要队尾出队。始终保持队中元素从队头到队尾单调递减。
        # 依序遍历一次数组，队头就是每个滑动窗口的最大值所在下标。
        # 时间复杂度分析：
        #   遍历中，每个元素最多进队一次，出队一次，故时间复杂度为 O(n)。
        
        from collections import deque
        dq = deque()
        result = []

        for i in range(len(nums)):
            
            if dq and dq[0] == i - k:
                # 出队头
                dq.popleft()
                
            while dq and nums[dq[-1]] <= nums[i]:
                # 出队尾
                dq.pop()
                
            dq.append(i)
            
            # 填充结果
            if i >= k - 1:
                result.append(nums[dq[0]])
                
        return result
    