# Median is the middle value in an ordered integer list. 
# If the size of the list is even, there is no middle value. 
# So the median is the mean of the two middle value.
# For example,
# [2,3,4], the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5
# Design a data structure that supports the following two operations:
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
 
# Example:
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
 
# Follow up:
# If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

from heapq import heappush,heappop
class MedianFinder(object):
        #双堆 O(nlogn)
        # 建立一个大根堆，一个小根堆。
        # 大根堆存储小于当前中位数，小根堆存储大于等于当前中位数。
        # 且小根堆的大小永远都比大根堆大1或相等。
        # 根据上述定义，我们每次可以通过小根堆的堆顶或者两个堆的堆顶元素的平均数求出中位数。
        # 维护时，如果新加入的元素大于等于当前的中位数，则加入小根堆；否则加入大根堆。
        # 然后如果发现两个堆的大小关系不满足上述要求，则可以通过弹出一个堆的元素放到另一个堆中。
        # 时间复杂度
        # 每次维护堆的时间为O(logn)，取出中位数的时间为O(1)。
        # 故总时间复杂度为O(nlogn)。

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = [] # for half left
        self.min_heap = [] # for half right

        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        left_size = len(self.max_heap)
        right_size = len(self.min_heap)
        if left_size == 0 and right_size == 0:
            heappush(self.min_heap, num)
            return

        if self.max_heap:
            left_val = -self.max_heap[0]
        if self.min_heap:
            right_val = self.min_heap[0]

        if left_size == right_size:
            if num <= left_val:
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)
        elif left_size > right_size:
            if num >= left_val:
                heappush(self.min_heap, num) # then balance
            else:
                tmp = heappop(self.max_heap)
                heappush(self.min_heap, -tmp)
                heappush(self.max_heap, -num)
        else: # left_size < right_size
            if num < right_val:
                heappush(self.max_heap, -num) # then balance
            else:
                tmp = heappop(self.min_heap)
                heappush(self.max_heap, -tmp)
                heappush(self.min_heap, num)

    def findMedian(self):
        """
        :rtype: float
        """
        left_size = len(self.max_heap)
        right_size = len(self.min_heap)

        if left_size == right_size:
            return (-self.max_heap[0] + self.min_heap[0])/2.0
        elif left_size > right_size:
            return float(-self.max_heap[0])
        else:
            return float(self.min_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
