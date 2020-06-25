# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
# find the minimum number of conference rooms required.

# Example 1:
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

# Example 2:
# Input: [[7,10],[2,4]]
# Output: 1

# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

# Hints:
# Think about how we would approach this problem in a very simplistic way. 
# We will allocate rooms to meetings that occur earlier in the day v/s the ones that occur later on, right?
# If you've figured out that we have to sort the meetings by their start time, 
# the next thing to think about is how do we do the allocation? 
# There are two scenarios possible here for any meeting. 
# Either there is no meeting room available and a new one has to be allocated, 
# or a meeting room has freed up and this meeting can take place there.
# An important thing to note is that 
# we don't really care which room gets freed up while allocating a room for the current meeting. 
# As long as a room is free, our job is done. 
# We already know the rooms we have allocated till now 
# and we also know when are they due to get free because of the end times of the meetings going on in those rooms. 
# We can simply check the room which is due to get vacated the earliest amongst all the allocated rooms.
# Following up on the previous hint, we can make use of a min-heap to store the end times of the meetings in various rooms. 
# So, every time we want to check if any room is free or not, 
# simply check the topmost element of the min heap as that would be the room 
# that would get free the earliest out of all the other rooms currently occupied. 
# If the room we extracted from the top of the min heap isn't free, 
# then no other room is. So, we can save time here and simply allocate a new room.

import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Heapq 优先队列 最小堆 O(nlgn)
        # 先把所有的时间区间按照起始时间排序，
        # 然后新建一个最小堆，开始遍历时间区间，如果堆不为空，且首元素小于等于当前区间的起始时间，去掉堆中的首元素，把当前区间的结束时间压入堆，
        # 由于最小堆是小的在前面，那么假如首元素小于等于起始时间，说明上一个会议已经结束，可以用该会议室开始下一个会议了，
        # 所以不用分配新的会议室，遍历完成后堆中元素的个数即为需要的会议室的个数。

        if not intervals:
            return 0
        intervals.sort(key = lambda i: i[0])
        heap = [intervals[0][1]]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i][1])
            else:
                heapq.heappush(heap, intervals[i][1])
        return len(heap)
        