# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
# determine if a person could attend all meetings.

# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:
# Input: [[7,10],[2,4]]
# Output: true

# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # M1. 蛮力算法 O(n^2) Time Limit Exceeded
        # 每两个区间比较一下，看是否有 overlap，有的话直接返回 false 。
        # 比较两个区间a和b是否有 overlap，可以检测两种情况，
        # 如果a的起始位置大于等于b的起始位置，且此时a的起始位置小于b的结束位置，则一定有 overlap，
        # 另一种情况是a和b互换个位置，如果b的起始位置大于等于a的起始位置，且此时b的起始位置小于a的结束位置，那么一定有 overlap，

        # if not intervals:
        #     return True

        # for i in range(len(intervals)): 
        #     for j in range(i+1, len(intervals)):
        #         if (intervals[i][0] >= intervals[j][0] and intervals[i][0] < intervals[j][1])\
        #         or (intervals[j][0] >= intervals[i][0] and intervals[j][0] < intervals[i][1]):
        #             return False

        # return True
        

        # M2. 排序检查 O(nlgn)
        # 先给所有区间排个序，用起始时间的先后来排，
        # 然后从第二个区间开始，如果开始时间早于前一个区间的结束时间，则说明会议时间有冲突，返回 false，
        # 遍历完成后没有冲突，则返回 true。

        if not intervals:
            return True

        intervals.sort(key=lambda interval: interval[0])
        preEnd = intervals[0][1]
        
        for interval in intervals[1:]:
            if interval[0] < preEnd:
                return False
            preEnd = interval[1]

        return True
        