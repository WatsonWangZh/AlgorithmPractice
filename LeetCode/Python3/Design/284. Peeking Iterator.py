# Given an Iterator class interface with methods: next() and hasNext(), 
# design and implement a PeekingIterator that support the peek() operation -- 
# it essentially peek() at the element that will be returned by the next call to next().

# Example:
# Assume that the iterator is initialized to the beginning of the list: [1,2,3].
# Call next() gets you 1, the first element in the list.
# Now you call peek() and it returns 2, the next element.
# Calling next() after that still return 2. 
# You call next() the final time and it returns 3, the last element. 
# Calling hasNext() after that should return false.

# Follow up: How would you extend your design to be generic 
# and work with all types, not just integer?

# Below is the interface for Iterator, which is already defined for you.

# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """

#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """

#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:

    # 这道题让我们实现一个顶端迭代器，在普通的迭代器类Iterator的基础上增加了peek的功能，
    # 就是返回查看下一个值的功能，但是不移动指针，next()函数才会移动指针，
    # 那我们可以定义一个变量curr专门来保存下一个值，再调用原来的一些成员函数，就可以实现这个顶端迭代器了。
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.curr = self.iterator.next() if self.iterator.hasNext() else None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.curr
        

    def next(self):
        """
        :rtype: int
        """
        curr = self.curr
        self.curr = self.iterator.next() if self.iterator.hasNext() else None
        return curr
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curr != None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].