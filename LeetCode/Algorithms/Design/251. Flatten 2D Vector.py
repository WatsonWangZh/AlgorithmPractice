# Design and implement an iterator to flatten a 2d vector. 
# It should support the following operations: next and hasNext.

# Example:
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
# iterator.next(); // return 1
# iterator.next(); // return 2
# iterator.next(); // return 3
# iterator.hasNext(); // return true
# iterator.hasNext(); // return true
# iterator.next(); // return 4
# iterator.hasNext(); // return false
 
# Notes:
# Please remember to RESET your class variables declared in Vector2D, 
# as static/class variables are persisted across multiple test cases. 
# Please see here for more details.
# You may assume that next() call will always be valid, that is, 
# there will be at least a next element in the 2d vector when next() is called.
 
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.

# Hints:
# How many variables do you need to keep track?
# Two variables is all you need. Try with x and y.
# Beware of empty rows. It could be the first few rows.
# To write correct code, think about the invariant to maintain. What is it?
# The invariant is x and y must always point to a valid point in the 2d vector. 
# Should you maintain your invariant ahead of time or right when you need it?
# Not sure? Think about how you would implement hasNext(). Which is more complex?
# Common logic in two different places should be refactored into a common method.

# M1. 展成一维存储
# class Vector2D(object):

#     def __init__(self, v):
#         """
#         :type v: List[List[int]]
#         """
#         self.data = []
#         for item in v:
#             self.data += item
#         self.curr_index = 0

#     def next(self):
#         """
#         :rtype: int
#         """
#         tmp = self.data[self.curr_index]
#         self.curr_index += 1
#         return tmp

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return self.curr_index < len(self.data)

# M2. 存储形式不变，行列双变量控制访问
class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.row = 0
        self.col = 0
        self.vec = v

    def next(self):
        """
        :rtype: int
        """
        # Key Point
        if not self.hasNext():
            return

        item = self.vec[self.row][self.col]
        self.col += 1
        return item

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True
            else:
                self.col = 0
                self.row += 1
                
        return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()