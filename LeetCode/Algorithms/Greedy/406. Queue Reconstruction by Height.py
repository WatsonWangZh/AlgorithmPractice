# Suppose you have a random list of people standing in a queue. 
# Each person is described by a pair of integers (h, k), 
# where h is the height of the person and k is the number of people 
# in front of this person who have a height greater than or equal to h. 
# Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

# Hints:
# What can you say about the position of the shortest person? 
# If the position of the shortest person is i, 
# how many people would be in front of the shortest person?
# Once you fix the position of the shortest person, 
# what can you say about the position of the second shortest person?

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 贪心 O(n^2)
        # 思路：身高高的人只会看到比他高的人，所以当身高高的人固定好了位置，前面插入多少个矮的人都不会破坏高的人的条件限制。
        # 所以应该先决定高的人的位置，再决定矮的人的位置；高的人限制条件少，矮的人限制条件多。
        # 先按身高从大到小排序，身高一样则按照k排序：身高大或k小意味着限制条件少，应该被优先考虑。
        # 依次插入元素：由上一点，先进入res的元素不会被后进入的元素影响，因此每一次插入只需要考虑自己不需要考虑别人。
        # 当遍历到元素[a,b]的时候，比它大的元素已经进组，比它小的元素还没进组，那么它应该插到res的第b位，从而实现0到b-1的数字都比它大。

        # 多级排序 先按身高降序排序，相同身高的按其前面的人数升序排序
        people.sort(key= lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
        

        # https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/cong-cha-ru-pai-xu-dao-tui-jie-fa-by-terjer7/
        # 从插入排序倒推解法
        people.sort(key=lambda p: p[1], reverse=True)
        people.sort(key=lambda p: p[0])

        res = []
        for p in reversed(people):
            if p[1] == 0: 
                res.append(p)
            else: 
                res.insert(-p[1], p)

        res.reverse()
        
        return res
