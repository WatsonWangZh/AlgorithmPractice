# Given two 1d vectors, implement an iterator to return their elements alternately.

# Example:
# Input:
# v1 = [1,2]
# v2 = [3,4,5,6] 
# Output: [1,3,2,4,5,6]

# Explanation: By calling next repeatedly until hasNext returns false, 
#              the order of elements returned by next should be: [1,3,2,4,5,6].

# Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

# Clarification for the follow up question:
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. 
# If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

# Input:
# [1,2,3]
# [4,5,6,7]
# [8,9]
# Output: [1,4,8,2,5,9,3,6,7].

# M1. 保存成要求格式正常访问
# class ZigzagIterator(object):

    # def __init__(self, v1, v2):
    #     """
    #     Initialize your data structure here.
    #     :type v1: List[int]
    #     :type v2: List[int]
    #     """
    #     self.data = []
    #     l = min(len(v1), len(v2))
    #     i = 0
    #     while i < l:
    #         self.data.append(v1[i])
    #         self.data.append(v2[i])
    #         i+=1
    #     if i != len(v1):
    #         self.data += v1[i:]
    #     elif i != len(v2):
    #         self.data += v2[i:]

    # def next(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.data.pop(0)

    # def hasNext(self):
    #     """
    #     :rtype: bool
    #     """
    #     if self.data:
    #         return True
    #     return False

# M2. 双变量控制访问
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.p1 = 0
        self.p2 = 0
        self.len1 = len(v1)
        self.len2 = len(v2)

    def next(self):
        """
        :rtype: int
        """
        if self.p1 < self.len1 and (self.p1 <= self.p2 or self.p2 >= self.len2):
            ans = self.v1[self.p1]
            self.p1 += 1
            return ans
        else:
            ans = self.v2[self.p2]
            self.p2 += 1
            return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.p1 < self.len1 or self.p2 < self.len2:
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())