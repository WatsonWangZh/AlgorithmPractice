# Given a data stream input of non-negative integers a1, a2, ..., an, ..., 
# summarize the numbers seen so far as a list of disjoint intervals.
# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
 
# Follow up:
# What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?

class unionFindSet:
    def __init__(self):
        self.root = {}
        self.intervals = {}

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu==pv:
                return False
        self.root[pu] = pv
        u_interval = self.intervals[pu]
        del self.intervals[pu]
        self.intervals[pv] = [min(self.intervals[pv][0], u_interval[0]), max(self.intervals[pv][1], u_interval[1])]
        return True

    def find(self, u):
        if u not in self.root:
                return -1
        path = []
        while self.root[u] != u:
                path.append(u)
                u = self.root[u]
        for p in path:
                self.root[p] = u
        return u

    def add(self, k):
        self.root[k] = k
        self.intervals[k] = [k,k]

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.uf = unionFindSet()

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.uf.root: ##dplicate 
                return
        self.uf.add(val)
        if val-1 in self.uf.root:
                self.uf.union(val, val-1)
        if val+1 in self.uf.root:
                self.uf.union(val, val+1)

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return sorted(self.uf.intervals.values())


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()