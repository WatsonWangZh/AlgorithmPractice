# Given a nested list of integers, implement an iterator to flatten it.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Example 1:
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, 
#              the order of elements returned by next should be: [1,1,2,1,1].

# Example 2:
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, 
#              the order of elements returned by next should be: [1,4,6].

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# M1. 迭代方式
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.nestedList.pop(0).getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.nestedList:
            if self.nestedList[0].isInteger():
                return True
            self.nestedList = self.nestedList[0].getList() + self.nestedList[1:]
        return False

# M2. DFS预处理方式
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flatten = []
        self.dfs(nestedList)
    
    def dfs(self, nestedList):
        for x in nestedList:
            if x.isInteger():
                self.flatten.append(x.getInteger())
            else:
                self.dfs(x.getList())

    def next(self):
        """
        :rtype: int
        """
        return self.flatten.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.flatten

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())